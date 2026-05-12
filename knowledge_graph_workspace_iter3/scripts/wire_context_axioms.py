#!/usr/bin/env python3
"""
Iter-3 Type-A orphan fix.

The bulk import creates an axiom node for every entry in a chain's
``**Axioms:**`` line, but those axioms are only wired into the graph if
they also appear as inputs to step 1.  Chains often list "context axioms"
that motivate the theorem without being literal step inputs — those nodes
end up as orphans.

This script re-parses the draft files, and for each chain, finds the
technique used in step 1 and adds an implicit input edge from any axiom
listed in ``**Axioms:**`` that isn't already wired to that technique
within the chain's theorem context.

Effect: orphan-axiom count drops; giant-component fraction rises.

Idempotent: skips edges that already exist (same from/to/used_in_theorem
combination).
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path("/Users/primetrce/Documents/maths")
WS = ROOT / "knowledge_graph_workspace_iter3"
DRAFTS = WS / "drafts"
GRAPH_PATH = ROOT / "knowledge_graph.json"
LOG_PATH = WS / "checks" / "wire_context_axioms.md"

RE_HEADING = re.compile(r"^###\s+(?P<name>.+?)\s*$")
RE_TERMINAL = re.compile(
    r"^\*\*Terminal:\*\*\s*`(?P<id>s_[A-Za-z0-9_]+)`", re.IGNORECASE
)
RE_AXIOMS = re.compile(r"^\*\*Axioms:\*\*\s*(?P<rest>.+)$", re.IGNORECASE)
RE_STEPS_HEAD = re.compile(r"^\*\*Steps:\*\*\s*$", re.IGNORECASE)
RE_TECH_USED_HEAD = re.compile(r"^\*\*Techniques used:\*\*", re.IGNORECASE)
RE_BACKTICK_S = re.compile(r"`(s_[A-Za-z0-9_]+)`")
RE_STEP = re.compile(
    r"input:\s*(?P<lhs>.+?)\s*--\[\s*(?P<tech>t_[A-Za-z0-9_]+)\s*(?P<body>\{.*?)?\s*\]-->\s*output:\s*`(?P<out>s_[A-Za-z0-9_]+)`",
    re.DOTALL,
)
RE_HR = re.compile(r"^---\s*$")
RE_NEXT_SECTION = re.compile(r"^##[^#]")


def parse_chains(path: Path):
    if not path.exists():
        return []
    chains = []
    cur_name = None
    cur_lines: list[str] = []

    def flush():
        nonlocal cur_name, cur_lines
        if cur_name is None:
            return
        terminal = None
        axioms: list[str] = []
        steps_lines: list[str] = []
        in_steps = False
        for line in cur_lines:
            if (m := RE_TERMINAL.match(line)):
                terminal = m.group("id")
                continue
            if (m := RE_AXIOMS.match(line)):
                axioms = RE_BACKTICK_S.findall(m.group("rest"))
                continue
            if RE_STEPS_HEAD.match(line):
                in_steps = True
                continue
            if RE_TECH_USED_HEAD.match(line):
                in_steps = False
                continue
            if in_steps:
                steps_lines.append(line)
        body_text = "\n".join(steps_lines)
        first_tech = None
        first_step_inputs: list[str] = []
        all_step_inputs: set[str] = set()
        m = RE_STEP.search(body_text)
        if m:
            first_tech = m.group("tech")
            first_step_inputs = RE_BACKTICK_S.findall(m.group("lhs"))
        for sm in RE_STEP.finditer(body_text):
            for inp in RE_BACKTICK_S.findall(sm.group("lhs")):
                all_step_inputs.add(inp)
        if terminal and first_tech and axioms:
            chains.append(
                {
                    "name": cur_name,
                    "terminal": terminal,
                    "axioms": axioms,
                    "first_tech": first_tech,
                    "first_step_inputs": first_step_inputs,
                    "all_step_inputs": all_step_inputs,
                    "source_file": path.name,
                }
            )
        cur_name = None
        cur_lines = []

    text = path.read_text(encoding="utf-8")
    for line in text.split("\n"):
        if (m := RE_HEADING.match(line)):
            flush()
            cur_name = m.group("name").strip()
            cur_lines = []
            continue
        if cur_name is not None and (RE_HR.match(line) or RE_NEXT_SECTION.match(line)):
            flush()
            continue
        if cur_name is not None:
            cur_lines.append(line)
    flush()
    return chains


def main():
    graph = json.loads(GRAPH_PATH.read_text())
    nodes_by_id = {n["id"]: n for n in graph["nodes"]}
    edges = graph["edges"]

    # Index existing edges by (from, to, used_in_theorem)
    edge_keys: set[tuple[str, str, str | None]] = set()
    for e in edges:
        edge_keys.add((e["from"], e["to"], e.get("used_in_theorem")))

    # Next edge id
    max_e = 0
    for e in edges:
        em = re.match(r"^e_(\d+)$", e.get("id", ""))
        if em:
            max_e = max(max_e, int(em.group(1)))

    added = 0
    added_per_area: dict[str, int] = defaultdict(int)

    for path in sorted(DRAFTS.glob("area_*_chains.md")):
        m = re.match(r"^area_(?P<area>[A-Z]+)_chains\.md$", path.name)
        area = m.group("area") if m else "??"
        chains = parse_chains(path)
        for c in chains:
            term = c["terminal"]
            tech = c["first_tech"]
            for ax in c["axioms"]:
                if ax in c["all_step_inputs"]:
                    continue  # already an input somewhere in the chain
                if ax not in nodes_by_id:
                    continue  # never created (shouldn't happen)
                key = (ax, tech, term)
                if key in edge_keys:
                    continue
                max_e += 1
                edges.append(
                    {
                        "id": f"e_{max_e:05d}",
                        "from": ax,
                        "to": tech,
                        "role": "input",
                        "parameter_binding": "{implicit: context_axiom}",
                        "used_in_theorem": term,
                        "source": f"iter3:{area}:context_wire",
                    }
                )
                edge_keys.add(key)
                added += 1
                added_per_area[area] += 1

    # Persist
    graph["metadata"].setdefault("phase_c_iter3", {})
    graph["metadata"]["phase_c_iter3"]["context_axiom_edges_added"] = added

    GRAPH_PATH.write_text(json.dumps(graph, indent=2, ensure_ascii=False))

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text(
        "# Wire Context Axioms\n\n"
        f"Total edges added: **{added}**\n\n"
        + "\n".join(f"- {a}: {n}" for a, n in sorted(added_per_area.items()))
    )
    print(f"Context-axiom edges added: {added}")
    for a, n in sorted(added_per_area.items()):
        print(f"  {a}: {n}")


if __name__ == "__main__":
    main()
