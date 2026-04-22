#!/usr/bin/env python3
"""
Phase B bulk import: merge the five Phase-B brief-catalog skeleton files
(areas D, E, F, G, H = 231 skeletons total) into knowledge_graph.json.

Each skeleton follows:
    ### <Theorem name>
    **Terminal:** `s_<theorem_id>`
    **Axioms:** `s_a`, `s_b`
    **Steps:**
    1. input: `⟨s_a, s_b⟩` --[t_technique {param: val}]--> output: `s_<theorem_id>`

Variants tolerated:
  - Single axiom without ⟨⟩: input: `s_a` --[t_...]--> output: `s_x`
  - Empty parameter binding: --[t_technique]-->
  - Multi-axiom list comma-separated inside ⟨...⟩
  - Optional  '*(already canonical)*' annotation after terminal id.

Behavior:
  1. Parses all 5 files.
  2. Creates terminal theorem node (kind=theorem) if new.
  3. Creates any missing axiom nodes (kind=axiom).
  4. Creates intermediate state nodes on demand (kind=state) -- expected zero
     for pure one-step skeletons.
  5. Per step: emits input edges from each axiom input → technique, and an
     output edge from technique → theorem. Each edge carries
        used_in_theorem, parameter_binding (dict or {}), and
        source: "brief_catalog".
  6. Validates technique id exists in graph; else logs and skips the step.
  7. Dedupes: if a terminal id already exists, skip creation; still emit the
     edges. Also flag near-duplicate axiom/theorem names.
  8. Runs integrity checks; every new theorem reaches ≥1 axiom via reverse BFS.
  9. Writes log to bulk_import_phase_b.md.
"""

from __future__ import annotations

import json
import re
from collections import deque, defaultdict
from pathlib import Path

# ---------------------------------------------------------------- paths

ROOT = Path("/Users/primetrce/Documents/maths")
WS = ROOT / "knowledge_graph_workspace_iter2"
GRAPH_PATH = ROOT / "knowledge_graph.json"

AREA_FILES = [
    ("D", WS / "brief_catalog_skeletons_area_D.md"),
    ("E", WS / "brief_catalog_skeletons_area_E.md"),
    ("F", WS / "brief_catalog_skeletons_area_F.md"),
    ("G", WS / "brief_catalog_skeletons_area_G.md"),
    ("H", WS / "brief_catalog_skeletons_area_H.md"),
]
LOG_PATH = WS / "bulk_import_phase_b.md"

# ---------------------------------------------------------------- regex

# Level-3 heading.  Handles optional trailing annotation like "*(already canonical)*".
RE_HEAD = re.compile(r"^###\s+(?P<name>.+?)\s*$")

RE_TERMINAL_LINE = re.compile(
    r"^\*\*Terminal:\*\*\s*`(?P<id>s_[A-Za-z0-9_]+)`(?:\s*\*\(.*?\)\*)?\s*$",
    re.IGNORECASE,
)
RE_AXIOMS_LINE = re.compile(r"^\*\*Axioms:\*\*\s*(?P<rest>.+)$", re.IGNORECASE)
RE_STEPS_LINE = re.compile(r"^\*\*Steps:\*\*\s*$", re.IGNORECASE)

RE_BACKTICK_ID = re.compile(r"`([ts]_[A-Za-z0-9_]+)`")

# Match one step. lhs up to --[, tech id, optional {body}, closing ]--, output.
#
# The body capture must tolerate nested braces inside the prose, e.g.
#   {target: "K_{3,3} subdivisions"}
# We therefore consume everything up to the mandatory  ` ]-->`  closer
# (optional whitespace before `]`), rather than a greedy-balanced block.
# `body` holds the raw "{...}" text (brace included) if present, else None.
RE_STEP_ARROW = re.compile(
    r"input:\s*(?P<lhs>.+?)\s*--\[\s*(?P<tech>t_[A-Za-z0-9_]+)\s*(?P<body>\{.*?)?\s*\]-->\s*output:\s*`(?P<out>s_[A-Za-z0-9_]+)`",
    re.DOTALL,
)
RE_NUMBERED_STEP = re.compile(r"^\s*\d+\.\s+(?P<body>.+)$")

# Second-level section heading (used to know if we've left the current
# theorem's steps block). Example: "## Set Theory".
RE_SECTION_HEAD = re.compile(r"^##[^#]")

# ---------------------------------------------------------------- helpers


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
    if raw in alias_to_id:
        return alias_to_id[raw]
    return raw


def next_edge_start(g: dict) -> int:
    max_n = 0
    for e in g["edges"]:
        m = re.match(r"^e_(\d+)$", e.get("id", ""))
        if m:
            n = int(m.group(1))
            if n > max_n:
                max_n = n
    return max_n


def parse_param_body(body: str | None) -> dict:
    """Store free-form param text as a single 'note' / key:value dict."""
    if not body:
        return {}
    s = body.strip()
    if s.startswith("{") and s.endswith("}"):
        s = s[1:-1].strip()
    if not s:
        return {}
    if ":" in s:
        k, _, v = s.partition(":")
        k = k.strip()
        k = re.sub(r"[^A-Za-z0-9_]", "_", k) or "note"
        return {k: v.strip()}
    return {"note": s}


def split_inputs(lhs: str) -> list[str]:
    """Extract all s_/t_ ids from the lhs (supports ⟨...⟩ bundles)."""
    if "⟨" in lhs or "," in lhs:
        return re.findall(r"\b([ts]_[A-Za-z0-9_]+)\b", lhs)
    ids = RE_BACKTICK_ID.findall(lhs)
    if ids:
        return ids
    return re.findall(r"\b([ts]_[A-Za-z0-9_]+)\b", lhs)


def humanize(nid: str) -> str:
    s = nid
    if s.startswith("s_") or s.startswith("t_"):
        s = s[2:]
    return s.replace("_", " ")


# ---------------------------------------------------------------- parser


def parse_skeletons(md_text: str) -> list[dict]:
    """Walk an area markdown file, emitting one record per ### theorem block
    with fields: name, terminal, axioms[], steps[{inputs,technique,params_raw,output}]."""
    sections: list[dict] = []
    cur: dict | None = None
    in_steps = False

    for raw in md_text.splitlines():
        line = raw.rstrip()

        m_head = RE_HEAD.match(line)
        if m_head:
            # Only accept headings that have a subsequent **Terminal:** line.
            # We flush the previous one only if it was complete.
            if cur is not None and cur.get("terminal") is not None:
                sections.append(cur)
            cur = {
                "name": re.sub(r"\s*\(already canonical\)\s*$", "", m_head.group("name").strip()),
                "terminal": None,
                "axioms": [],
                "steps": [],
            }
            in_steps = False
            continue

        if cur is None:
            continue

        # A section heading (## ...) or another ### resets the steps-collection.
        if RE_SECTION_HEAD.match(line):
            # end current theorem and flush if usable
            if cur.get("terminal") is not None:
                sections.append(cur)
            cur = None
            in_steps = False
            continue

        m_term = RE_TERMINAL_LINE.match(line)
        if m_term:
            cur["terminal"] = m_term.group("id")
            in_steps = False
            continue

        m_ax = RE_AXIOMS_LINE.match(line)
        if m_ax:
            cur["axioms"] = RE_BACKTICK_ID.findall(m_ax.group("rest"))
            in_steps = False
            continue

        if RE_STEPS_LINE.match(line):
            in_steps = True
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
            # non-numbered lines inside steps are ignored

    if cur is not None and cur.get("terminal") is not None:
        sections.append(cur)

    return sections


# ---------------------------------------------------------------- dedup


def near_duplicate(new_name: str, nodes_by_id, skip_id: str | None = None) -> list[tuple[str, str]]:
    """Return (id, name) pairs whose name is a case-insensitive substring match
    for new_name (either direction). Skips tiny tokens and the subject itself."""
    out = []
    low = new_name.lower().strip()
    if not low or len(low) < 6:
        return out
    for nid, node in nodes_by_id.items():
        if nid == skip_id:
            continue
        nname = (node.get("name") or "").lower().strip()
        if not nname or len(nname) < 6:
            continue
        if low == nname:
            out.append((nid, node["name"]))
            continue
        if low in nname or nname in low:
            out.append((nid, node["name"]))
    return out


# ---------------------------------------------------------------- fan-in audit


def top_techniques(edges: list[dict], k: int = 10) -> list[tuple[str, int]]:
    """Return top-k techniques by total incident-edge count (fan-in+fan-out)."""
    counts: dict[str, int] = defaultdict(int)
    for e in edges:
        if e["from"].startswith("t_"):
            counts[e["from"]] += 1
        if e["to"].startswith("t_"):
            counts[e["to"]] += 1
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:k]


def fan_in_only(edges: list[dict], k: int = 10) -> list[tuple[str, int]]:
    """Fan-in: incoming edges (role=input) = edges pointing TO a technique."""
    counts: dict[str, int] = defaultdict(int)
    for e in edges:
        if e["to"].startswith("t_"):
            counts[e["to"]] += 1
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:k]


# ---------------------------------------------------------------- main


def main() -> None:
    graph = load_graph()
    nodes_by_id, alias_to_id = build_indices(graph)

    baseline_nodes = len(graph["nodes"])
    baseline_edges = len(graph["edges"])

    technique_ids = {n["id"] for n in graph["nodes"] if n["kind"] == "technique"}

    # ------- fan-in snapshot BEFORE import -------
    fan_in_before_bundle = top_techniques(graph["edges"], k=10)
    fan_in_before_pure = fan_in_only(graph["edges"], k=10)

    # ------- parse all skeletons -------
    all_sections: list[tuple[str, dict]] = []
    per_area_count: dict[str, int] = {}
    for area, path in AREA_FILES:
        txt = path.read_text()
        parsed = parse_skeletons(txt)
        per_area_count[area] = len(parsed)
        for s in parsed:
            all_sections.append((area, s))

    # ------- bookkeeping -------
    new_theorems: list[str] = []
    new_states: list[str] = []
    new_axioms: list[str] = []
    new_edges_added = 0
    unknown_techs: list[dict] = []        # {chain, step_idx, tech, area}
    dup_flags: list[dict] = []

    edge_counter = next_edge_start(graph)

    def make_edge_id() -> str:
        nonlocal edge_counter
        edge_counter += 1
        return f"e_{edge_counter:04d}"

    # ------- declared-kind map (axiom vs theorem vs state) -------
    declared_kind: dict[str, str] = {}

    def set_kind(nid: str, k: str):
        # theorem > axiom > state: an id declared as an axiom on the **Axioms:**
        # line must not be downgraded to "state" just because it also appears
        # as an input on the steps line (which it always does).
        priority = {"state": 1, "axiom": 2, "theorem": 3}
        if nid not in declared_kind:
            declared_kind[nid] = k
        else:
            if priority[k] > priority[declared_kind[nid]]:
                declared_kind[nid] = k

    for _area, sec in all_sections:
        for a in sec["axioms"]:
            set_kind(a, "axiom")
        if sec["terminal"]:
            set_kind(sec["terminal"], "theorem")
        for st in sec["steps"]:
            for i in st["inputs"]:
                set_kind(i, "state")
            set_kind(st["output"], "state")
        if sec["terminal"]:
            declared_kind[sec["terminal"]] = "theorem"

    # ------- walk sections -------
    for area, sec in all_sections:
        theorem_id = resolve_id(sec["terminal"], nodes_by_id, alias_to_id)

        # Collision check: theorem id must not already be an axiom or state.
        existing = nodes_by_id.get(theorem_id)
        if existing is not None and existing["kind"] in ("axiom", "state"):
            # Log as a dup flag (id collision — shouldn't happen for brief catalog)
            dup_flags.append({
                "kind": "theorem_id_collision",
                "id": theorem_id,
                "existing_kind": existing["kind"],
                "existing_name": existing.get("name"),
                "new_name": sec["name"],
                "area": area,
            })

        # Ensure theorem node exists
        if theorem_id not in nodes_by_id:
            node = {
                "id": theorem_id,
                "kind": "theorem",
                "name": sec["name"],
                "description": f"Imported from Phase B brief catalog area {area}.",
                "source": "brief_catalog",
            }
            graph["nodes"].append(node)
            nodes_by_id[theorem_id] = node
            new_theorems.append(theorem_id)
            dups = near_duplicate(sec["name"], nodes_by_id, skip_id=theorem_id)
            if dups:
                dup_flags.append({
                    "kind": "theorem_name_near_dup",
                    "new_id": theorem_id,
                    "new_name": sec["name"],
                    "matches": dups,
                    "area": area,
                })

        # Ensure axiom nodes exist
        for ax_raw in sec["axioms"]:
            ax_id = resolve_id(ax_raw, nodes_by_id, alias_to_id)
            if ax_id not in nodes_by_id:
                kind = declared_kind.get(ax_id, "axiom")
                name = humanize(ax_id)
                node = {
                    "id": ax_id,
                    "kind": kind,
                    "name": name,
                    "description": f"Imported from Phase B brief catalog area {area} as {kind}.",
                    "source": "brief_catalog",
                }
                graph["nodes"].append(node)
                nodes_by_id[ax_id] = node
                if kind == "axiom":
                    new_axioms.append(ax_id)
                elif kind == "theorem":
                    new_theorems.append(ax_id)
                else:
                    new_states.append(ax_id)
                dups = near_duplicate(name, nodes_by_id, skip_id=ax_id)
                if dups:
                    dup_flags.append({
                        "kind": "axiom_name_near_dup",
                        "new_id": ax_id,
                        "new_name": name,
                        "matches": dups,
                        "area": area,
                    })

        # Walk steps
        used_input_ids: set[str] = set()
        first_tech: str | None = None
        for idx, step in enumerate(sec["steps"], start=1):
            tech_id = step["technique"]
            if tech_id not in technique_ids:
                unknown_techs.append({
                    "area": area,
                    "chain": sec["name"],
                    "step_idx": idx,
                    "tech": tech_id,
                })
                continue

            if first_tech is None:
                first_tech = tech_id

            param_binding = parse_param_body(step["params_raw"])

            # Ensure input state/axiom nodes exist
            input_ids = [resolve_id(x, nodes_by_id, alias_to_id) for x in step["inputs"]]
            for iid in input_ids:
                used_input_ids.add(iid)
                if iid not in nodes_by_id:
                    kind = declared_kind.get(iid, "state")
                    if iid == theorem_id:
                        kind = "theorem"
                    name = humanize(iid)
                    node = {
                        "id": iid,
                        "kind": kind,
                        "name": name,
                        "description": f"Imported from Phase B brief catalog area {area} as {kind}.",
                        "source": "brief_catalog",
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
                    dups = near_duplicate(name, nodes_by_id, skip_id=iid)
                    if dups:
                        dup_flags.append({
                            "kind": "input_name_near_dup",
                            "new_id": iid,
                            "new_name": name,
                            "matches": dups,
                            "area": area,
                        })

            # Ensure output node exists (it should be the theorem, but tolerate)
            out_id = resolve_id(step["output"], nodes_by_id, alias_to_id)
            if out_id not in nodes_by_id:
                kind = "theorem" if out_id == theorem_id else declared_kind.get(out_id, "state")
                name = sec["name"] if out_id == theorem_id else humanize(out_id)
                node = {
                    "id": out_id,
                    "kind": kind,
                    "name": name,
                    "description": f"Imported from Phase B brief catalog area {area} as {kind}.",
                    "source": "brief_catalog",
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

            # Emit input edges
            for iid in input_ids:
                graph["edges"].append({
                    "id": make_edge_id(),
                    "from": iid,
                    "to": tech_id,
                    "role": "input",
                    "parameter_binding": param_binding,
                    "used_in_theorem": theorem_id,
                    "source": "brief_catalog",
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
                "source": "brief_catalog",
            })
            new_edges_added += 1

        # Ensure every declared axiom actually appears as an input. If not, add
        # a declared-axiom edge to the first technique of the chain (so no
        # declared axiom becomes a dangling node).
        declared_axioms = [resolve_id(a, nodes_by_id, alias_to_id) for a in sec["axioms"]]
        if first_tech is not None:
            for ax in declared_axioms:
                if ax not in used_input_ids:
                    graph["edges"].append({
                        "id": make_edge_id(),
                        "from": ax,
                        "to": first_tech,
                        "role": "input",
                        "parameter_binding": {"role": "declared_axiom"},
                        "used_in_theorem": theorem_id,
                        "source": "brief_catalog",
                    })
                    new_edges_added += 1

    # ---------------------------------------------------------------- checks

    incoming_by_to = defaultdict(int)
    for e in graph["edges"]:
        incoming_by_to[e["to"]] += 1

    theorems_without_incoming = [t for t in new_theorems if incoming_by_to.get(t, 0) < 1]

    # Every new node has ≥1 incident edge
    incident = defaultdict(int)
    for e in graph["edges"]:
        incident[e["from"]] += 1
        incident[e["to"]] += 1

    new_state_axiom_ids = list(set(new_states) | set(new_axioms))
    states_without_incident = [s for s in new_state_axiom_ids if incident.get(s, 0) < 1]

    # Reverse BFS: from every new theorem, can we reach an axiom?
    rev_adj: dict[str, list[str]] = defaultdict(list)
    for e in graph["edges"]:
        rev_adj[e["to"]].append(e["from"])

    axiom_ids = {n["id"] for n in graph["nodes"] if n["kind"] == "axiom"}

    unreachable_theorems: list[str] = []
    for t in new_theorems:
        seen = set()
        q = deque([t])
        reached = False
        while q:
            x = q.popleft()
            if x in seen:
                continue
            seen.add(x)
            if x in axiom_ids and x != t:
                reached = True
                break
            for y in rev_adj.get(x, ()):
                if y not in seen:
                    q.append(y)
        if not reached:
            unreachable_theorems.append(t)

    # ---------------------------------------------------------------- metadata

    graph["metadata"]["phase_b_bulk_import"] = {
        "date": "2026-04-22",
        "skeletons_ingested_per_area": per_area_count,
        "skeletons_ingested_total": len(all_sections),
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

    save_graph(graph)

    # ---------------------------------------------------------------- fan-in AFTER

    fan_in_after_bundle = top_techniques(graph["edges"], k=10)
    fan_in_after_pure = fan_in_only(graph["edges"], k=10)

    # Unify: show before/after for the union of top-10s
    bundle_before = {k: v for k, v in fan_in_before_bundle}
    bundle_after = {k: v for k, v in fan_in_after_bundle}
    pure_before = {k: v for k, v in fan_in_before_pure}
    pure_after = {k: v for k, v in fan_in_after_pure}

    bundle_union = sorted(
        set(bundle_before.keys()) | set(bundle_after.keys()),
        key=lambda t: -(bundle_after.get(t, 0)),
    )[:10]
    pure_union = sorted(
        set(pure_before.keys()) | set(pure_after.keys()),
        key=lambda t: -(pure_after.get(t, 0)),
    )[:10]

    # ---------------------------------------------------------------- log

    lines: list[str] = []
    lines.append("# Phase B Bulk Import Log")
    lines.append("")
    lines.append("Automated merge of the five Phase-B brief-catalog skeleton files")
    lines.append("(areas D, E, F, G, H) into `knowledge_graph.json`.")
    lines.append("")
    lines.append("## Per-area skeletons ingested")
    lines.append("")
    for area, path in AREA_FILES:
        lines.append(f"- Area **{area}** ({path.name}): **{per_area_count.get(area, 0)}**")
    lines.append(f"- **Total:** **{len(all_sections)}**")
    lines.append("")

    lines.append("## Counts")
    lines.append("")
    lines.append(f"- Baseline nodes: **{baseline_nodes}**")
    lines.append(f"- Baseline edges: **{baseline_edges}**")
    lines.append(f"- New theorem nodes added: **{len(new_theorems)}**")
    lines.append(f"- New axiom nodes added:   **{len(new_axioms)}**")
    lines.append(f"- New state nodes added:   **{len(new_states)}**")
    lines.append(f"- New edges added:         **{new_edges_added}**")
    lines.append(f"- Final nodes: **{len(graph['nodes'])}**")
    lines.append(f"- Final edges: **{len(graph['edges'])}**")
    lines.append("")

    lines.append("## New theorems")
    lines.append("")
    for t in new_theorems:
        lines.append(f"- `{t}` — {nodes_by_id[t].get('name', '(no name)')}")
    lines.append("")

    lines.append("## New axioms")
    lines.append("")
    for t in new_axioms:
        lines.append(f"- `{t}` — {nodes_by_id[t].get('name', '(no name)')}")
    lines.append("")

    lines.append("## New states")
    lines.append("")
    if new_states:
        for t in new_states:
            lines.append(f"- `{t}` — {nodes_by_id[t].get('name', '(no name)')}")
    else:
        lines.append("_None. (Pure one-step skeletons expected to add only theorems + axioms.)_")
    lines.append("")

    lines.append("## Unknown technique references (skipped steps)")
    lines.append("")
    if unknown_techs:
        for u in unknown_techs:
            lines.append(
                f"- area {u['area']}, chain **{u['chain']}**, step {u['step_idx']}: `{u['tech']}`"
            )
    else:
        lines.append("_None — every referenced technique id exists in the graph._")
    lines.append("")

    lines.append("## Dedup / near-duplicate flags")
    lines.append("")
    if dup_flags:
        for f in dup_flags:
            if f["kind"] == "theorem_id_collision":
                lines.append(
                    f"- id collision `{f['id']}`: existing kind `{f['existing_kind']}` \"{f['existing_name']}\" "
                    f"vs new theorem \"{f['new_name']}\" (area {f['area']})"
                )
            else:
                matches = "; ".join(f"`{mid}` \"{mname}\"" for mid, mname in f["matches"])
                lines.append(
                    f"- ({f['kind']}) `{f['new_id']}` \"{f['new_name']}\"  ⇔  {matches}  (area {f['area']})"
                )
    else:
        lines.append("_None._")
    lines.append("")

    lines.append("## Integrity checks")
    lines.append("")
    lines.append(f"- New theorems with zero incoming edges: **{len(theorems_without_incoming)}**")
    for t in theorems_without_incoming:
        lines.append(f"  - `{t}`")
    lines.append(f"- New state/axiom nodes with zero incident edges: **{len(states_without_incident)}**")
    for s in states_without_incident:
        lines.append(f"  - `{s}`")
    lines.append(f"- New theorems unreachable from any axiom (reverse BFS): **{len(unreachable_theorems)}**")
    for t in unreachable_theorems:
        lines.append(f"  - `{t}`")
    lines.append("")

    lines.append("## Fan-in audit (top 10 techniques by incoming edge count) — pure fan-in")
    lines.append("")
    lines.append("| technique | before | after | Δ |")
    lines.append("| --- | ---: | ---: | ---: |")
    for tid in pure_union:
        b = pure_before.get(tid, 0)
        a = pure_after.get(tid, 0)
        lines.append(f"| `{tid}` | {b} | {a} | +{a - b} |")
    lines.append("")

    lines.append("## Fan-in audit — total incident edges (in + out) on each technique")
    lines.append("")
    lines.append("| technique | before | after | Δ |")
    lines.append("| --- | ---: | ---: | ---: |")
    for tid in bundle_union:
        b = bundle_before.get(tid, 0)
        a = bundle_after.get(tid, 0)
        lines.append(f"| `{tid}` | {b} | {a} | +{a - b} |")
    lines.append("")

    LOG_PATH.write_text("\n".join(lines))

    # ---------------------------------------------------------------- stdout

    print("=" * 60)
    print("Phase B bulk import complete.")
    print(f"  Baseline: {baseline_nodes} nodes, {baseline_edges} edges")
    print(f"  Per-area skeletons: {per_area_count}")
    print(f"  Total skeletons:    {len(all_sections)}")
    print(f"  Added: {len(new_theorems)} theorems, {len(new_axioms)} axioms, "
          f"{len(new_states)} states, {new_edges_added} edges")
    print(f"  Unknown techniques: {len(unknown_techs)}")
    print(f"  Dedup flags:        {len(dup_flags)}")
    print(f"  Theorems with no in-edge:          {len(theorems_without_incoming)}")
    print(f"  Nodes with no incident edge:       {len(states_without_incident)}")
    print(f"  Theorems unreachable from axioms:  {len(unreachable_theorems)}")
    print(f"  Final: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges")
    print("=" * 60)


if __name__ == "__main__":
    main()
