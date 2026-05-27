#!/usr/bin/env python3
"""
Iter-3 integrity audit: orphan detection, connected-component analysis,
duplicate-id check, and typed-correctness sanity for the expanded graph.

Outputs:
  - checks/audit_iter3.md (report)
  - prints summary to stdout
"""

from __future__ import annotations

import json
import re
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path("/Users/primetrce/Documents/maths")
GRAPH = ROOT / "knowledge_graph.json"
LOG = ROOT / "knowledge_graph_workspace_iter3" / "checks" / "audit_iter3.md"


def main():
    g = json.loads(GRAPH.read_text())
    nodes = g["nodes"]
    edges = g["edges"]

    by_kind = defaultdict(int)
    for n in nodes:
        by_kind[n["kind"]] += 1

    nodes_by_id = {n["id"]: n for n in nodes}

    # ---- duplicate id check
    seen_ids = defaultdict(int)
    for n in nodes:
        seen_ids[n["id"]] += 1
    dup_ids = {i: c for i, c in seen_ids.items() if c > 1}

    # ---- orphan check: nodes with no incident edge
    incident = defaultdict(int)
    for e in edges:
        incident[e["from"]] += 1
        incident[e["to"]] += 1
    orphans = [n["id"] for n in nodes if incident[n["id"]] == 0]
    orphans_by_kind = defaultdict(list)
    for oid in orphans:
        orphans_by_kind[nodes_by_id[oid]["kind"]].append(oid)

    # ---- connected components (undirected)
    adj: dict[str, set[str]] = defaultdict(set)
    for e in edges:
        adj[e["from"]].add(e["to"])
        adj[e["to"]].add(e["from"])

    seen: set[str] = set()
    components = []
    for n in nodes:
        nid = n["id"]
        if nid in seen:
            continue
        comp = []
        q = deque([nid])
        seen.add(nid)
        while q:
            x = q.popleft()
            comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    q.append(y)
        components.append(comp)
    components.sort(key=len, reverse=True)
    giant = components[0]
    giant_pct = 100.0 * len(giant) / len(nodes)

    # ---- theorem nodes lacking any incoming edge (i.e., no derivation)
    incoming = defaultdict(int)
    for e in edges:
        incoming[e["to"]] += 1
    theorems_no_incoming = [
        n["id"] for n in nodes if n["kind"] == "theorem" and incoming[n["id"]] == 0
    ]

    # ---- axioms that aren't used as input anywhere
    outgoing = defaultdict(int)
    for e in edges:
        outgoing[e["from"]] += 1
    unused_axioms = [
        n["id"] for n in nodes if n["kind"] == "axiom" and outgoing[n["id"]] == 0
    ]

    # ---- techniques with low fan-in/out
    tech_fan = defaultdict(lambda: {"in": 0, "out": 0})
    for e in edges:
        if e["from"].startswith("t_"):
            tech_fan[e["from"]]["out"] += 1
        if e["to"].startswith("t_"):
            tech_fan[e["to"]]["in"] += 1
    cold_techs = [
        (t, fan["in"], fan["out"])
        for t, fan in tech_fan.items()
        if fan["in"] + fan["out"] < 3
    ]

    # ---- write report
    lines = [
        "# Iter-3 Integrity Audit",
        "",
        f"**Graph file:** `{GRAPH}` ({GRAPH.stat().st_size / 1024 / 1024:.1f} MB)",
        "",
        "## Node counts",
        "",
        f"- Total nodes: {len(nodes)}",
        f"- Axioms     : {by_kind.get('axiom', 0)}",
        f"- States     : {by_kind.get('state', 0)}",
        f"- Theorems   : {by_kind.get('theorem', 0)}",
        f"- Techniques : {by_kind.get('technique', 0)}",
        f"- Total edges: {len(edges)}",
        "",
        "## Duplicate id check",
        "",
        f"- Duplicate ids: {len(dup_ids)}",
    ]
    if dup_ids:
        for i, c in list(dup_ids.items())[:20]:
            lines.append(f"  - `{i}` × {c}")
        if len(dup_ids) > 20:
            lines.append(f"  - … and {len(dup_ids) - 20} more")

    lines.extend([
        "",
        "## Orphan nodes (no incident edges)",
        "",
        f"- Total orphans: {len(orphans)}",
    ])
    for k in ("axiom", "state", "theorem", "technique"):
        if orphans_by_kind.get(k):
            lines.append(f"  - {k}: {len(orphans_by_kind[k])}")

    lines.extend([
        "",
        "## Connected components",
        "",
        f"- Components: {len(components)}",
        f"- Giant component size: {len(giant)} / {len(nodes)} = {giant_pct:.2f}%",
        f"- Singletons (size 1): {sum(1 for c in components if len(c) == 1)}",
        f"- Other small components (size 2–10): {sum(1 for c in components if 2 <= len(c) <= 10)}",
    ])

    lines.extend([
        "",
        "## Theorems with no incoming edge (no derivation recorded)",
        "",
        f"- Count: {len(theorems_no_incoming)}",
    ])
    for tid in theorems_no_incoming[:20]:
        lines.append(f"  - `{tid}`")
    if len(theorems_no_incoming) > 20:
        lines.append(f"  - … and {len(theorems_no_incoming) - 20} more")

    lines.extend([
        "",
        "## Axioms with no outgoing edge (unused)",
        "",
        f"- Count: {len(unused_axioms)}",
    ])
    for aid in unused_axioms[:20]:
        lines.append(f"  - `{aid}`")
    if len(unused_axioms) > 20:
        lines.append(f"  - … and {len(unused_axioms) - 20} more")

    lines.extend([
        "",
        "## Low-fan techniques (fan-in + fan-out < 3)",
        "",
        f"- Count: {len(cold_techs)} of {by_kind.get('technique', 0)}",
    ])
    for t, fi, fo in sorted(cold_techs, key=lambda x: x[1] + x[2]):
        lines.append(f"  - `{t}` : in={fi}, out={fo}")

    LOG.write_text("\n".join(lines))

    # Console summary
    print(f"Nodes: {len(nodes)}  Edges: {len(edges)}")
    print(f"  axiom={by_kind.get('axiom', 0)}  state={by_kind.get('state', 0)}  theorem={by_kind.get('theorem', 0)}  technique={by_kind.get('technique', 0)}")
    print(f"Duplicate ids: {len(dup_ids)}")
    print(f"Orphans: {len(orphans)}  (singleton components: {sum(1 for c in components if len(c) == 1)})")
    print(f"Giant component: {len(giant)} / {len(nodes)} ({giant_pct:.2f}%)")
    print(f"Theorems with no incoming edge: {len(theorems_no_incoming)}")
    print(f"Unused axioms: {len(unused_axioms)}")
    print(f"Report: {LOG}")


if __name__ == "__main__":
    main()
