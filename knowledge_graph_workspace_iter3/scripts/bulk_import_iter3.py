#!/usr/bin/env python3
"""
Phase C / iter-3 bulk import.

Parses the per-domain chain files in ``knowledge_graph_workspace_iter3/drafts/``
and appends new theorem / state / axiom nodes and the edges connecting them
to ``knowledge_graph.json``.

Chain format (output by 13 parallel agents + the NT pilot):

    ### <theorem name> (cite: <url>)
    **Axioms:** `s_a`, `s_b`
    **Terminal:** `s_theorem_id` (kind: theorem)
    **Steps:**
    1. input: `⟨s_a, s_b⟩` --[t_technique {param: value}]--> output: `s_intermediate`
    2. input: `s_intermediate` --[t_other_technique]--> output: `s_theorem_id`
    **Techniques used:** t_a, t_b

Tolerant of mild format drift (missing cite, missing "(kind: theorem)" tag,
single-input without ⟨⟩, empty parameter binding, multi-line steps).

Output:
  - rewrites knowledge_graph.json with a new ``phase_c_iter3`` metadata block.
  - writes a per-domain stats log to ``checks/bulk_import_iter3.md``.
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path("/Users/primetrce/Documents/maths")
WS = ROOT / "knowledge_graph_workspace_iter3"
DRAFTS = WS / "drafts"
GRAPH_PATH = ROOT / "knowledge_graph.json"
LOG_PATH = WS / "checks" / "bulk_import_iter3.md"

# ----------------------------------------------------------------- regex

RE_HEADING = re.compile(r"^###\s+(?P<name>.+?)\s*$")
RE_CITE = re.compile(r"\(cite:\s*(?P<url>https?://\S+?)\s*\)\s*$", re.IGNORECASE)
RE_TERMINAL = re.compile(
    r"^\*\*Terminal:\*\*\s*`(?P<id>s_[A-Za-z0-9_]+)`",
    re.IGNORECASE,
)
RE_AXIOMS = re.compile(r"^\*\*Axioms:\*\*\s*(?P<rest>.+)$", re.IGNORECASE)
RE_STEPS_HEAD = re.compile(r"^\*\*Steps:\*\*\s*$", re.IGNORECASE)
RE_TECH_USED_HEAD = re.compile(r"^\*\*Techniques used:\*\*", re.IGNORECASE)

RE_BACKTICK_S_ID = re.compile(r"`(s_[A-Za-z0-9_]+)`")
RE_BACKTICK_T_ID = re.compile(r"`?(t_[A-Za-z0-9_]+)`?")

# A single step. Tolerates nested braces in the body (parameter binding).
# Captures: lhs (everything between `input:` and `--[`), tech id, optional
# brace-body, and output state id.
RE_STEP = re.compile(
    r"input:\s*(?P<lhs>.+?)\s*--\[\s*(?P<tech>t_[A-Za-z0-9_]+)\s*(?P<body>\{.*?)?\s*\]-->\s*output:\s*`(?P<out>s_[A-Za-z0-9_]+)`",
    re.DOTALL,
)
RE_NUMBERED_STEP_LINE = re.compile(r"^\s*\d+\.\s+(?P<body>.+)$")

# Where a chain block ends. The block ends when:
#   - We see a new ### heading
#   - We see `**Techniques used:**`
#   - We see a `---` separator
#   - We see `## ` (next section)
RE_NEXT_HEADING = re.compile(r"^###\s+")
RE_HR = re.compile(r"^---\s*$")
RE_NEXT_SECTION = re.compile(r"^##[^#]")


# ----------------------------------------------------------------- IO

def load_graph() -> dict:
    with GRAPH_PATH.open() as f:
        return json.load(f)


def save_graph(g: dict) -> None:
    with GRAPH_PATH.open("w") as f:
        json.dump(g, f, indent=2, ensure_ascii=False)


# ----------------------------------------------------------------- parsing

class Chain:
    __slots__ = ("name", "cite", "terminal", "axioms", "steps", "techniques", "source_file")

    def __init__(self):
        self.name: str = ""
        self.cite: str | None = None
        self.terminal: str | None = None
        self.axioms: list[str] = []
        # each step: (inputs: list[str], tech: str, body: str|None, output: str)
        self.steps: list[tuple[list[str], str, str | None, str]] = []
        self.techniques: list[str] = []
        self.source_file: str = ""


def parse_axioms_line(rest: str) -> list[str]:
    ids = RE_BACKTICK_S_ID.findall(rest)
    # Filter junk like the literal "s_axiom_one" placeholder if any.
    return [i for i in ids if not i.endswith(("_one", "_two")) or i.startswith("s_axiom_")]


def parse_step_body(body_text: str) -> list[tuple[list[str], str, str | None, str]]:
    """Parse 1+ step matches in concatenated body text."""
    out = []
    for m in RE_STEP.finditer(body_text):
        lhs = m.group("lhs").strip()
        inputs = RE_BACKTICK_S_ID.findall(lhs)
        tech = m.group("tech")
        body = m.group("body")
        # body may include "{...}" or fragments; truncate to balanced { ... } at first level
        out_id = m.group("out")
        out.append((inputs, tech, body, out_id))
    return out


def parse_chain_block(name: str, lines: list[str], src: str) -> Chain | None:
    """Parse the lines belonging to a single chain (between two `###` headings)."""
    c = Chain()
    c.name = name
    c.source_file = src

    # 1) Cite (if present, embedded in name line).
    m = RE_CITE.search(name)
    if m:
        c.cite = m.group("url")
        c.name = RE_CITE.sub("", name).strip()

    in_steps = False
    step_buf: list[str] = []

    for raw in lines:
        line = raw.rstrip("\n")

        # Terminal
        m = RE_TERMINAL.match(line)
        if m:
            c.terminal = m.group("id")
            continue

        # Axioms
        m = RE_AXIOMS.match(line)
        if m:
            c.axioms = parse_axioms_line(m.group("rest"))
            continue

        # Steps section start
        if RE_STEPS_HEAD.match(line):
            in_steps = True
            continue

        # Techniques used line stops the steps section.
        if RE_TECH_USED_HEAD.match(line):
            in_steps = False
            # parse technique ids on this line and possibly next
            for t in RE_BACKTICK_T_ID.findall(line):
                c.techniques.append(t)
            continue

        if in_steps:
            step_buf.append(line)

    body_text = "\n".join(step_buf)
    c.steps = parse_step_body(body_text)

    if not c.terminal or not c.steps:
        return None

    return c


def parse_area_file(path: Path) -> list[Chain]:
    """Walk an area_X_chains.md file and emit Chain objects."""
    chains: list[Chain] = []
    if not path.exists():
        return chains

    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    cur_name: str | None = None
    cur_lines: list[str] = []

    def flush():
        nonlocal cur_name, cur_lines
        if cur_name is None:
            return
        ch = parse_chain_block(cur_name, cur_lines, path.name)
        if ch is not None:
            chains.append(ch)
        cur_name = None
        cur_lines = []

    for line in lines:
        m = RE_HEADING.match(line)
        if m:
            flush()
            cur_name = m.group("name").strip()
            cur_lines = []
            continue
        # End-of-chain sentinels:
        if cur_name is not None and (RE_HR.match(line) or RE_NEXT_SECTION.match(line)):
            # Don't stop on every "---" — the chain body may end at ---. Flush.
            flush()
            continue
        if cur_name is not None:
            cur_lines.append(line)

    flush()
    return chains


# ----------------------------------------------------------------- integration

def integrate(chains_per_area: dict[str, list[Chain]], graph: dict) -> dict:
    """Append nodes & edges from chains into ``graph``. Returns stats dict."""

    nodes_by_id: dict[str, dict] = {n["id"]: n for n in graph["nodes"]}
    edges = graph.setdefault("edges", [])

    valid_tech_ids = {n["id"] for n in graph["nodes"] if n["kind"] == "technique"}

    # Next edge id
    max_e = 0
    for e in edges:
        em = re.match(r"^e_(\d+)$", e.get("id", ""))
        if em:
            max_e = max(max_e, int(em.group(1)))

    stats = {
        "by_area": defaultdict(lambda: defaultdict(int)),
        "skipped_dup_theorem": [],
        "unknown_tech": defaultdict(int),
        "created_axioms": 0,
        "created_states": 0,
        "created_theorems": 0,
        "created_edges": 0,
        "chains_processed": 0,
    }

    def ensure_node(node_id: str, kind: str, *, default_name: str | None = None) -> dict:
        if node_id in nodes_by_id:
            return nodes_by_id[node_id]
        name = default_name or node_id[2:].replace("_", " ")
        node = {
            "id": node_id,
            "kind": kind,
            "name": name,
            "type_signature": "MathObject",
            "description": f"Iter-3 imported {kind} ({node_id}).",
        }
        if kind == "theorem":
            node["source"] = "iter3"
        graph["nodes"].append(node)
        nodes_by_id[node_id] = node
        if kind == "axiom":
            stats["created_axioms"] += 1
        elif kind == "state":
            stats["created_states"] += 1
        elif kind == "theorem":
            stats["created_theorems"] += 1
        return node

    def new_edge_id() -> str:
        nonlocal max_e
        max_e += 1
        return f"e_{max_e:05d}"

    for area, chains in chains_per_area.items():
        for c in chains:
            stats["chains_processed"] += 1
            area_stats = stats["by_area"][area]

            # Terminal — if it already exists in graph (canonical_node_index),
            # we still want to wire the chain to it; only skip wiring if the
            # terminal is already a theorem AND already has incident edges.
            term = c.terminal
            existed = term in nodes_by_id
            if existed and nodes_by_id[term]["kind"] == "theorem":
                term_has_edges = any(
                    e["from"] == term or e["to"] == term for e in edges
                )
                if term_has_edges:
                    stats["skipped_dup_theorem"].append((area, c.name, term))
                    area_stats["skipped_dup"] += 1
                    continue

            term_node = ensure_node(term, "theorem", default_name=c.name)
            if c.cite:
                term_node.setdefault("citations", []).append(c.cite)
            term_node.setdefault("iter3_areas", []).append(area)

            # Axioms
            for ax in c.axioms:
                ensure_node(ax, "axiom")

            # Steps: build intermediate states + edges
            for (inputs, tech, body, out_id) in c.steps:
                if tech not in valid_tech_ids:
                    stats["unknown_tech"][tech] += 1
                    area_stats["unknown_tech_count"] += 1
                    continue

                # Inputs: if a referenced state is unknown, treat it as state node.
                for inp in inputs:
                    if inp not in nodes_by_id:
                        # If it's also an axiom on the chain's axioms list, mark axiom
                        if inp in c.axioms:
                            ensure_node(inp, "axiom")
                        else:
                            ensure_node(inp, "state")

                # Output: terminal is theorem (already ensured); else state.
                if out_id == term:
                    # already exists as theorem; we'll point edge there
                    pass
                else:
                    if out_id not in nodes_by_id:
                        ensure_node(out_id, "state")

                # parameter binding — best-effort: keep the raw body text.
                pb = body.strip() if body else ""

                # Emit input edges
                for inp in inputs:
                    e_in = {
                        "id": new_edge_id(),
                        "from": inp,
                        "to": tech,
                        "role": "input",
                        "parameter_binding": pb,
                        "used_in_theorem": term,
                        "source": f"iter3:{area}",
                    }
                    edges.append(e_in)
                    stats["created_edges"] += 1

                # Emit output edge
                e_out = {
                    "id": new_edge_id(),
                    "from": tech,
                    "to": out_id,
                    "role": "output",
                    "parameter_binding": pb,
                    "used_in_theorem": term,
                    "source": f"iter3:{area}",
                }
                edges.append(e_out)
                stats["created_edges"] += 1

            area_stats["chains_integrated"] += 1

    return stats


# ----------------------------------------------------------------- main

def main():
    if not GRAPH_PATH.exists():
        sys.exit(f"Graph file not found: {GRAPH_PATH}")

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    chains_per_area: dict[str, list[Chain]] = {}
    for p in sorted(DRAFTS.glob("area_*_chains.md")):
        m = re.match(r"^area_(?P<area>[A-Z0-9]+)_chains\.md$", p.name)
        if not m:
            continue
        area = m.group("area")
        chains = parse_area_file(p)
        chains_per_area[area] = chains
        print(f"Parsed {len(chains):4d} chains from {p.name}", flush=True)

    total = sum(len(v) for v in chains_per_area.values())
    print(f"Total chains parsed: {total}", flush=True)

    graph = load_graph()
    pre_nodes = len(graph["nodes"])
    pre_edges = len(graph.get("edges", []))

    stats = integrate(chains_per_area, graph)

    # Metadata block
    graph["metadata"]["phase_c_iter3"] = {
        "date": "2026-05-12",
        "chains_per_area": {k: len(v) for k, v in chains_per_area.items()},
        "chains_processed": stats["chains_processed"],
        "created_axioms": stats["created_axioms"],
        "created_states": stats["created_states"],
        "created_theorems": stats["created_theorems"],
        "created_edges": stats["created_edges"],
        "skipped_dup_count": len(stats["skipped_dup_theorem"]),
        "unknown_tech_count": sum(stats["unknown_tech"].values()),
    }

    save_graph(graph)

    post_nodes = len(graph["nodes"])
    post_edges = len(graph["edges"])

    # Log
    lines = [
        "# Iter-3 Bulk Import Log",
        "",
        f"Pre-integration : {pre_nodes} nodes, {pre_edges} edges",
        f"Post-integration: {post_nodes} nodes, {post_edges} edges",
        "",
        f"Chains processed     : {stats['chains_processed']}",
        f"Created theorem nodes: {stats['created_theorems']}",
        f"Created state nodes  : {stats['created_states']}",
        f"Created axiom nodes  : {stats['created_axioms']}",
        f"Created edges        : {stats['created_edges']}",
        f"Skipped (already had edges): {len(stats['skipped_dup_theorem'])}",
        f"Unknown techniques   : {sum(stats['unknown_tech'].values())}",
        "",
        "## Per-area",
        "",
        "| Area | Chains parsed | Integrated | Skipped dup | Unknown tech |",
        "|---|---|---|---|---|",
    ]
    for area, chains in chains_per_area.items():
        a = stats["by_area"][area]
        lines.append(
            f"| {area} | {len(chains)} | {a.get('chains_integrated', 0)} | {a.get('skipped_dup', 0)} | {a.get('unknown_tech_count', 0)} |"
        )

    if stats["unknown_tech"]:
        lines.extend(["", "## Unknown technique counts", ""])
        for t, n in sorted(stats["unknown_tech"].items(), key=lambda x: -x[1]):
            lines.append(f"- `{t}` × {n}")

    if stats["skipped_dup_theorem"]:
        lines.extend(["", "## Skipped duplicate theorems (already wired)", ""])
        for area, name, tid in stats["skipped_dup_theorem"][:50]:
            lines.append(f"- [{area}] `{tid}` ({name})")
        if len(stats["skipped_dup_theorem"]) > 50:
            lines.append(f"- … and {len(stats['skipped_dup_theorem']) - 50} more")

    LOG_PATH.write_text("\n".join(lines))
    print(f"\nLog written: {LOG_PATH}")
    print(f"Graph saved: {GRAPH_PATH}")


if __name__ == "__main__":
    main()
