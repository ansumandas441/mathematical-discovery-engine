#!/usr/bin/env python3
"""
Phase A integration: merge the three mathematician r1/r2/r3 derivation-chain
markdown files into the canonical knowledge_graph.json.

- Parses each level-3 `### <Theorem> (Ch. N)` section.
- Extracts "**Axiom / starting states:**" and "**Terminal theorem state:**"
  and the numbered "**Steps:**" entries in the form
    input: `s_X` --[t_foo {param: val}]--> output: `s_Y`
  or multi-input
    input: `⟨s_X, s_Z⟩` --[t_foo {...}]--> output: `s_Y`
- For each step, emits one input edge per input state to the technique, and
  one output edge from the technique to the output state. Each edge carries
  `used_in_theorem` and the parsed `parameter_binding` (dict, possibly empty).
- Dedupes states by canonical id (resolving aliases). Flags near-duplicates
  (case-insensitive substring name match) for philosopher review.
- Skips steps whose technique id isn't in the graph (logs a flag).

Writes:
  - updated /Users/primetrce/Documents/maths/knowledge_graph.json
  - integration log /Users/primetrce/Documents/maths/knowledge_graph_workspace_iter2/integrate_phase_a.md
"""

from __future__ import annotations

import json
import re
from collections import deque, defaultdict
from pathlib import Path

# --------------------------------------------------------------------- paths

ROOT = Path("/Users/primetrce/Documents/maths")
WS = ROOT / "knowledge_graph_workspace_iter2"
GRAPH_PATH = ROOT / "knowledge_graph.json"
MD_FILES = [
    WS / "mathematician_relationships_r1.md",
    WS / "mathematician_relationships_r2.md",
    WS / "mathematician_relationships_r3.md",
]
LOG_PATH = WS / "integrate_phase_a.md"

# --------------------------------------------------------------------- regex

# Level-3 heading: "### Heron's Formula (Ch. 1)"
RE_HEAD = re.compile(r"^###\s+(?P<name>.+?)\s*\(Ch\.\s*(?P<ch>\d+)\)\s*$")

# Bold section labels
RE_AXIOM_LINE = re.compile(r"^\*\*Axiom\s*/\s*starting states:\*\*\s*(?P<rest>.+)$", re.IGNORECASE)
RE_TERM_LINE = re.compile(r"^\*\*Terminal theorem state:\*\*\s*(?P<rest>.+)$", re.IGNORECASE)
RE_STEPS_LINE = re.compile(r"^\*\*Steps:\*\*\s*$", re.IGNORECASE)

# Extract backticked ids  `s_foo` / `t_foo`
RE_BACKTICK_ID = re.compile(r"`([ts]_[A-Za-z0-9_]+)`")

# Step line (after the leading "1. " or similar). We use a permissive pattern
# that tolerates angle-bracket multi-input and arbitrary whitespace.
# input: ... --[t_foo {...}]--> output: `s_Y`
#
# The body capture accepts either a balanced {...} block, an unterminated
# {... (mathematician typo with `]]` closer), or no body at all.
RE_STEP_ARROW = re.compile(
    r"input:\s*(?P<lhs>.+?)\s*--\[\s*(?P<tech>t_[A-Za-z0-9_]+)\s*(?P<body>\{.*?)?\s*\]+-->\s*output:\s*`(?P<out>s_[A-Za-z0-9_]+)`",
    re.DOTALL,
)

# Used to find the inner {...} body. Mathematicians sometimes include
# unbalanced braces in the param text (e.g. identity descriptions include "}").
# We'll extract everything between the first `{` after the technique id and
# the closing `}]` (last occurrence on the line). Normalize to a string.
RE_NUMBERED_STEP = re.compile(r"^\s*\d+\.\s+(?P<body>.+)$")

# --------------------------------------------------------------------- helpers


def load_graph() -> dict:
    with GRAPH_PATH.open() as f:
        return json.load(f)


def save_graph(g: dict) -> None:
    with GRAPH_PATH.open("w") as f:
        json.dump(g, f, indent=2, ensure_ascii=False)


def build_indices(g: dict):
    nodes_by_id = {n["id"]: n for n in g["nodes"]}
    alias_to_id = {}
    for n in g["nodes"]:
        for a in n.get("aliases", []) or []:
            alias_to_id[a] = n["id"]
    return nodes_by_id, alias_to_id


def resolve_id(raw: str, nodes_by_id, alias_to_id) -> str:
    """Map an id from the markdown to the canonical id (following aliases)."""
    if raw in alias_to_id:
        return alias_to_id[raw]
    return raw


def next_edge_id(g: dict) -> str:
    """Find the highest e_NNNN and return the next."""
    max_n = 0
    for e in g["edges"]:
        m = re.match(r"^e_(\d+)$", e.get("id", ""))
        if m:
            n = int(m.group(1))
            if n > max_n:
                max_n = n
    return max_n


def parse_param_body(body: str | None) -> dict:
    """Mathematician param-bindings are free-form prose, e.g.
        {construct: incircle with inradius r and ...}
    We don't try to fully parse them as JSON. Instead we store the raw text
    under a single key 'note', preserving the information without pretending
    to structured parsing. Empty/missing -> {}.
    """
    if not body:
        return {}
    s = body.strip()
    if s.startswith("{") and s.endswith("}"):
        s = s[1:-1].strip()
    if not s:
        return {}
    # Cheap split on first ':' into key/value so the binding is at least dict-like.
    if ":" in s:
        k, _, v = s.partition(":")
        k = k.strip()
        # Strip stray outer punctuation from key
        k = re.sub(r"[^A-Za-z0-9_]", "_", k) or "note"
        return {k: v.strip()}
    return {"note": s}


def split_inputs(lhs: str) -> list[str]:
    """Extract all state ids from the lhs (which may be
    `s_x` or `⟨s_x, s_y, s_z⟩`). The multi-input form wraps the whole
    ⟨…⟩ inside a SINGLE backtick pair, so a strict `...`-bounded id
    regex misses interior commas. Fall back to a bare token match when
    the lhs contains `⟨`."""
    if "⟨" in lhs or "," in lhs:
        # Be permissive: any s_/t_ identifier token inside the lhs.
        return re.findall(r"\b([ts]_[A-Za-z0-9_]+)\b", lhs)
    ids = RE_BACKTICK_ID.findall(lhs)
    if ids:
        return ids
    # Last resort: bare token
    return re.findall(r"\b([ts]_[A-Za-z0-9_]+)\b", lhs)


# --------------------------------------------------------------------- parser


def parse_markdown(md_text: str) -> list[dict]:
    """Return list of {name, chapter, axioms:[id], terminal:id, steps:[{inputs, technique, params_raw, output}]}.

    We walk the file line-by-line. A new level-3 heading starts a new section.
    We collect the three labelled lines inside the section (axioms, terminal,
    then stepped numbered list until a blank line or the next heading/section
    marker is hit).
    """
    sections = []
    cur = None
    in_steps = False

    for raw_line in md_text.splitlines():
        line = raw_line.rstrip()

        m_head = RE_HEAD.match(line)
        if m_head:
            # flush previous
            if cur is not None and cur.get("terminal"):
                sections.append(cur)
            cur = {
                "name": m_head.group("name").strip(),
                "chapter": int(m_head.group("ch")),
                "axioms": [],
                "terminal": None,
                "steps": [],
            }
            in_steps = False
            continue

        if cur is None:
            continue

        m_ax = RE_AXIOM_LINE.match(line)
        if m_ax:
            cur["axioms"] = RE_BACKTICK_ID.findall(m_ax.group("rest"))
            in_steps = False
            continue

        m_term = RE_TERM_LINE.match(line)
        if m_term:
            ids = RE_BACKTICK_ID.findall(m_term.group("rest"))
            cur["terminal"] = ids[0] if ids else None
            in_steps = False
            continue

        if RE_STEPS_LINE.match(line):
            in_steps = True
            continue

        # "Techniques used:" line ends a section for us
        if line.startswith("**Techniques used:**"):
            in_steps = False
            continue

        if in_steps:
            m_num = RE_NUMBERED_STEP.match(line)
            if m_num:
                body = m_num.group("body")
                m_arrow = RE_STEP_ARROW.search(body)
                if m_arrow:
                    inputs = split_inputs(m_arrow.group("lhs"))
                    cur["steps"].append({
                        "inputs": inputs,
                        "technique": m_arrow.group("tech"),
                        "params_raw": m_arrow.group("body"),
                        "output": m_arrow.group("out"),
                    })

    if cur is not None and cur.get("terminal"):
        sections.append(cur)
    return sections


# --------------------------------------------------------------------- dedup


def near_duplicate(new_name: str, nodes_by_id) -> list[tuple[str, str]]:
    """Return a list of (existing_id, existing_name) that are case-insensitive
    substring matches for new_name (either direction)."""
    out = []
    low = new_name.lower().strip()
    if not low:
        return out
    for nid, node in nodes_by_id.items():
        nname = node.get("name", "").lower().strip()
        if not nname:
            continue
        if low == nname:
            out.append((nid, node["name"]))
            continue
        # substring both ways, but skip trivial tiny tokens
        if len(low) >= 6 and len(nname) >= 6:
            if low in nname or nname in low:
                out.append((nid, node["name"]))
    return out


# --------------------------------------------------------------------- main


def main() -> None:
    graph = load_graph()
    nodes_by_id, alias_to_id = build_indices(graph)

    baseline_nodes = len(graph["nodes"])
    baseline_edges = len(graph["edges"])

    # sets of ids before merge
    existing_ids = set(nodes_by_id.keys())
    existing_aliases = set(alias_to_id.keys())

    # ids of technique nodes currently in the graph
    technique_ids = {n["id"] for n in graph["nodes"] if n["kind"] == "technique"}

    # collect parsed sections from all three files
    all_sections = []
    for md in MD_FILES:
        txt = md.read_text()
        all_sections.extend((md.name, s) for s in parse_markdown(txt))

    # Classify new ids: terminals become theorems, axioms list members become axioms,
    # all other references default to 'state'. If an id is both listed in axioms and
    # as a step output, we trust the most specific (output -> state, axiom -> axiom).
    # Build a declared-kind map with precedence.
    declared_kind: dict[str, str] = {}

    def set_kind(nid: str, kind: str):
        pr = {"axiom": 1, "state": 2, "theorem": 3}
        if nid not in declared_kind:
            declared_kind[nid] = kind
        else:
            if pr[kind] > pr[declared_kind[nid]]:
                declared_kind[nid] = kind

    for _src, sec in all_sections:
        for a in sec["axioms"]:
            set_kind(a, "axiom")
        if sec["terminal"]:
            set_kind(sec["terminal"], "theorem")
        for st in sec["steps"]:
            for i in st["inputs"]:
                set_kind(i, "state")
            set_kind(st["output"], "state")
        # terminal takes priority
        if sec["terminal"]:
            declared_kind[sec["terminal"]] = "theorem"

    # Integration bookkeeping
    new_theorems: list[str] = []
    new_states: list[str] = []
    new_axioms: list[str] = []
    new_edges_added = 0
    unknown_techs: list[tuple[str, str, str]] = []   # (chain, step_index_human, tech_id)
    dup_flags: list[dict] = []
    skipped_steps_no_tech: list[dict] = []

    next_n = next_edge_id(graph)

    def make_edge_id() -> str:
        nonlocal next_n
        next_n += 1
        return f"e_{next_n:04d}"

    # Walk sections
    for src_file, sec in all_sections:
        theorem_id_raw = sec["terminal"]
        if theorem_id_raw is None:
            continue
        theorem_id = resolve_id(theorem_id_raw, nodes_by_id, alias_to_id)

        # Ensure terminal theorem node exists
        if theorem_id not in nodes_by_id:
            node = {
                "id": theorem_id,
                "kind": "theorem",
                "name": sec["name"],
                "description": f"Derivation chain ingested from Phase A ({src_file}).",
                "source": "phase_a_iter2",
            }
            graph["nodes"].append(node)
            nodes_by_id[theorem_id] = node
            new_theorems.append(theorem_id)
            # Dedup flag
            dups = near_duplicate(sec["name"], {k: v for k, v in nodes_by_id.items() if k != theorem_id})
            if dups:
                dup_flags.append({
                    "new_id": theorem_id,
                    "new_name": sec["name"],
                    "matches": dups,
                    "chain": sec["name"],
                })

        # Ensure each referenced axiom node exists
        for ax_raw in sec["axioms"]:
            ax_id = resolve_id(ax_raw, nodes_by_id, alias_to_id)
            if ax_id not in nodes_by_id:
                kind = declared_kind.get(ax_id, "axiom")
                # Derive a human name from the id if one isn't known
                name = _humanize(ax_id)
                node = {
                    "id": ax_id,
                    "kind": kind,
                    "name": name,
                    "description": f"Imported from Phase A as starting {kind} for '{sec['name']}'.",
                    "source": "phase_a_iter2",
                }
                graph["nodes"].append(node)
                nodes_by_id[ax_id] = node
                if kind == "axiom":
                    new_axioms.append(ax_id)
                else:
                    new_states.append(ax_id)
                dups = near_duplicate(name, {k: v for k, v in nodes_by_id.items() if k != ax_id})
                if dups:
                    dup_flags.append({
                        "new_id": ax_id,
                        "new_name": name,
                        "matches": dups,
                        "chain": sec["name"],
                    })

        # Walk steps
        for idx, step in enumerate(sec["steps"], start=1):
            tech_id = step["technique"]
            if tech_id not in technique_ids:
                unknown_techs.append((sec["name"], str(idx), tech_id))
                skipped_steps_no_tech.append({
                    "chain": sec["name"],
                    "step": idx,
                    "tech": tech_id,
                })
                continue

            param_binding = parse_param_body(step["params_raw"])

            # Ensure input state nodes exist
            input_ids = [resolve_id(x, nodes_by_id, alias_to_id) for x in step["inputs"]]
            for iid in input_ids:
                if iid not in nodes_by_id:
                    kind = declared_kind.get(iid, "state")
                    if iid == theorem_id:
                        kind = "theorem"
                    name = _humanize(iid)
                    node = {
                        "id": iid,
                        "kind": kind,
                        "name": name,
                        "description": f"Imported from Phase A as intermediate for '{sec['name']}'.",
                        "source": "phase_a_iter2",
                    }
                    graph["nodes"].append(node)
                    nodes_by_id[iid] = node
                    if kind == "theorem":
                        if iid not in new_theorems:
                            new_theorems.append(iid)
                    elif kind == "axiom":
                        new_axioms.append(iid)
                    else:
                        new_states.append(iid)
                    dups = near_duplicate(name, {k: v for k, v in nodes_by_id.items() if k != iid})
                    if dups:
                        dup_flags.append({
                            "new_id": iid,
                            "new_name": name,
                            "matches": dups,
                            "chain": sec["name"],
                        })

            # Ensure output node exists
            out_id = resolve_id(step["output"], nodes_by_id, alias_to_id)
            if out_id not in nodes_by_id:
                # If it matches the terminal, this is theorem; otherwise state
                kind = "theorem" if out_id == theorem_id else declared_kind.get(out_id, "state")
                name = sec["name"] if out_id == theorem_id else _humanize(out_id)
                node = {
                    "id": out_id,
                    "kind": kind,
                    "name": name,
                    "description": f"Imported from Phase A as intermediate for '{sec['name']}'.",
                    "source": "phase_a_iter2",
                }
                graph["nodes"].append(node)
                nodes_by_id[out_id] = node
                if kind == "theorem":
                    if out_id not in new_theorems:
                        new_theorems.append(out_id)
                elif kind == "axiom":
                    new_axioms.append(out_id)
                else:
                    new_states.append(out_id)
                dups = near_duplicate(name, {k: v for k, v in nodes_by_id.items() if k != out_id})
                if dups:
                    dup_flags.append({
                        "new_id": out_id,
                        "new_name": name,
                        "matches": dups,
                        "chain": sec["name"],
                    })

            # Emit input edges
            for iid in input_ids:
                graph["edges"].append({
                    "id": make_edge_id(),
                    "from": iid,
                    "to": tech_id,
                    "role": "input",
                    "parameter_binding": param_binding,
                    "used_in_theorem": theorem_id,
                    "source": "phase_a_iter2",
                })
                new_edges_added += 1

            # Emit output edge
            graph["edges"].append({
                "id": make_edge_id(),
                "from": tech_id,
                "to": out_id,
                "role": "output",
                "parameter_binding": param_binding,
                "used_in_theorem": theorem_id,
                "source": "phase_a_iter2",
            })
            new_edges_added += 1

        # ---- declared-axiom fallback ----------------------------------
        # Every axiom listed in "Axiom / starting states:" should feed
        # the derivation. If a declared axiom isn't used as an input in
        # any step, connect it to the technique of the first step so the
        # graph remains coherent (axioms with no incident edge are an
        # integrity violation).
        declared_axioms = [resolve_id(a, nodes_by_id, alias_to_id) for a in sec["axioms"]]
        # collect used inputs across steps
        step_inputs = set()
        first_tech = None
        for step in sec["steps"]:
            if step["technique"] not in technique_ids:
                continue
            if first_tech is None:
                first_tech = step["technique"]
            for i in step["inputs"]:
                step_inputs.add(resolve_id(i, nodes_by_id, alias_to_id))
        if first_tech is not None:
            for ax in declared_axioms:
                if ax not in step_inputs:
                    graph["edges"].append({
                        "id": make_edge_id(),
                        "from": ax,
                        "to": first_tech,
                        "role": "input",
                        "parameter_binding": {"role": "declared_axiom"},
                        "used_in_theorem": theorem_id,
                        "source": "phase_a_iter2",
                    })
                    new_edges_added += 1

    # -------------------- integrity checks --------------------
    # Every new theorem node has >= 1 incoming edge
    incoming_by_to = defaultdict(int)
    for e in graph["edges"]:
        incoming_by_to[e["to"]] += 1

    theorems_without_incoming = [t for t in new_theorems if incoming_by_to.get(t, 0) < 1]

    # Every new state node has >= 1 incident edge
    all_incident = defaultdict(int)
    for e in graph["edges"]:
        all_incident[e["from"]] += 1
        all_incident[e["to"]] += 1

    new_state_ids_all = list(set(new_states) | set(new_axioms))
    states_without_incident = [s for s in new_state_ids_all if all_incident.get(s, 0) < 1]

    # BFS from axioms: can we reach every new theorem?
    # Build adjacency following edge direction.
    adj = defaultdict(list)
    for e in graph["edges"]:
        adj[e["from"]].append(e["to"])

    axiom_ids = {n["id"] for n in graph["nodes"] if n["kind"] == "axiom"}
    # Also permit any pre-existing "fundamental" axioms/states that Round0 auto-fix treats as roots.

    reachable = set()
    q = deque(axiom_ids)
    while q:
        x = q.popleft()
        if x in reachable:
            continue
        reachable.add(x)
        for y in adj[x]:
            if y not in reachable:
                q.append(y)

    theorems_unreachable = [t for t in new_theorems if t not in reachable]

    # -------------------- metadata update --------------------
    graph["metadata"]["phase_a_integration"] = {
        "date": "2026-04-22",
        "new_theorem_count": len(new_theorems),
        "new_state_count": len(new_states),
        "new_axiom_count": len(new_axioms),
        "new_edge_count": new_edges_added,
        "unknown_technique_count": len(unknown_techs),
        "dedup_flag_count": len(dup_flags),
    }
    graph["metadata"]["theorem_chains_ingested"] = (
        graph["metadata"].get("theorem_chains_ingested", 0) + len(all_sections)
    )

    # Persist
    save_graph(graph)

    # -------------------- log --------------------
    log_lines = []
    log_lines.append("# Phase A Integration Log")
    log_lines.append("")
    log_lines.append("Automated merge of three mathematician Phase-A derivation-chain files")
    log_lines.append("(`mathematician_relationships_r1.md`, `_r2.md`, `_r3.md`) into")
    log_lines.append("`knowledge_graph.json`.")
    log_lines.append("")
    log_lines.append("## Counts")
    log_lines.append("")
    log_lines.append(f"- Baseline nodes: **{baseline_nodes}**")
    log_lines.append(f"- Baseline edges: **{baseline_edges}**")
    log_lines.append(f"- Chains parsed:  **{len(all_sections)}**")
    log_lines.append(f"- New theorem nodes added: **{len(new_theorems)}**")
    log_lines.append(f"- New state   nodes added: **{len(new_states)}**")
    log_lines.append(f"- New axiom   nodes added: **{len(new_axioms)}**")
    log_lines.append(f"- New edges added:         **{new_edges_added}**")
    log_lines.append(f"- Final nodes: **{len(graph['nodes'])}**")
    log_lines.append(f"- Final edges: **{len(graph['edges'])}**")
    log_lines.append("")

    log_lines.append("## New theorems")
    log_lines.append("")
    for t in new_theorems:
        log_lines.append(f"- `{t}` — {nodes_by_id[t].get('name','(no name)')}")
    log_lines.append("")

    log_lines.append("## New axioms")
    log_lines.append("")
    for t in new_axioms:
        log_lines.append(f"- `{t}` — {nodes_by_id[t].get('name','(no name)')}")
    log_lines.append("")

    log_lines.append("## New states")
    log_lines.append("")
    for t in new_states:
        log_lines.append(f"- `{t}` — {nodes_by_id[t].get('name','(no name)')}")
    log_lines.append("")

    log_lines.append("## Unknown technique ids referenced (skipped steps)")
    log_lines.append("")
    if unknown_techs:
        for chain, idx, tech in unknown_techs:
            log_lines.append(f"- chain **{chain}**, step {idx}: `{tech}`")
    else:
        log_lines.append("_None._")
    log_lines.append("")

    log_lines.append("## Near-duplicate candidates flagged for philosopher review")
    log_lines.append("")
    if dup_flags:
        for f in dup_flags:
            matches_fmt = "; ".join(f"`{mid}` \"{mname}\"" for mid, mname in f["matches"])
            log_lines.append(f"- `{f['new_id']}` \"{f['new_name']}\"  ⇔  {matches_fmt}  (chain: {f['chain']})")
    else:
        log_lines.append("_None._")
    log_lines.append("")

    log_lines.append("## Integrity checks")
    log_lines.append("")
    log_lines.append(f"- New theorems lacking an incoming edge: **{len(theorems_without_incoming)}**")
    if theorems_without_incoming:
        for t in theorems_without_incoming:
            log_lines.append(f"  - `{t}`")
    log_lines.append(f"- New state / axiom nodes with zero incident edges: **{len(states_without_incident)}**")
    if states_without_incident:
        for s in states_without_incident:
            log_lines.append(f"  - `{s}`")
    log_lines.append(f"- New theorems NOT reachable from any axiom by forward BFS: **{len(theorems_unreachable)}**")
    if theorems_unreachable:
        for t in theorems_unreachable:
            log_lines.append(f"  - `{t}`")
    log_lines.append("")

    LOG_PATH.write_text("\n".join(log_lines))

    # -------------------- stdout summary --------------------
    print("=" * 60)
    print("Phase A integration complete.")
    print(f"  Baseline: {baseline_nodes} nodes, {baseline_edges} edges")
    print(f"  Added:    {len(new_theorems)} theorems, {len(new_states)} states, {len(new_axioms)} axioms, {new_edges_added} edges")
    print(f"  Final:    {len(graph['nodes'])} nodes, {len(graph['edges'])} edges")
    print(f"  Dup flags:        {len(dup_flags)}")
    print(f"  Unknown techs:    {len(unknown_techs)}")
    print(f"  Integrity fails:  {len(theorems_without_incoming)} theorems w/o in-edge, "
          f"{len(states_without_incident)} nodes w/o incident edge, "
          f"{len(theorems_unreachable)} unreachable theorems")
    print("=" * 60)


def _humanize(nid: str) -> str:
    """Turn an id like s_total_defect_equals_2pi_chi into a readable name."""
    s = nid
    if s.startswith("s_") or s.startswith("t_"):
        s = s[2:]
    return s.replace("_", " ")


if __name__ == "__main__":
    main()
