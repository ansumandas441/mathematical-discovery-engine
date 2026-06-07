import json, sys, os

GRAPH = "/Users/primetrce/Documents/maths/knowledge_graph.json"
WS = "/Users/primetrce/Documents/maths/knowledge_graph_workspace"

new_nodes = json.load(open(os.path.join(WS, "cinlar_new_nodes.json")))
edges_raw = json.load(open(os.path.join(WS, "cinlar_new_edges.json")))

d = json.load(open(GRAPH))
existing_ids = {n["id"] for n in d["nodes"]}

problems = []

# 1. node id uniqueness
for n in new_nodes:
    if n["id"] in existing_ids:
        problems.append("DUP NODE ID (already in graph): " + n["id"])
seen = set()
for n in new_nodes:
    if n["id"] in seen:
        problems.append("DUP within new nodes: " + n["id"])
    seen.add(n["id"])

all_ids = existing_ids | {n["id"] for n in new_nodes}
kind_of = {n["id"]: n["kind"] for n in d["nodes"]}
kind_of.update({n["id"]: n["kind"] for n in new_nodes})

# 2. validate endpoints exist + bipartite
for i, e in enumerate(edges_raw):
    f, t, role, thm = e["from"], e["to"], e["role"], e.get("used_in_theorem", "")
    if f not in all_ids:
        problems.append("edge %d missing from: %s" % (i, f)); continue
    if t not in all_ids:
        problems.append("edge %d missing to: %s" % (i, t)); continue
    if thm and thm not in all_ids:
        problems.append("edge %d missing used_in_theorem: %s" % (i, thm))
    kf, kt = kind_of[f], kind_of[t]
    if role == "input":
        if not (kf in ("state", "theorem", "axiom") and kt == "technique"):
            problems.append("edge %d bad input: %s(%s)->%s(%s)" % (i, f, kf, t, kt))
    elif role == "output":
        if not (kf == "technique" and kt in ("state", "theorem", "axiom")):
            problems.append("edge %d bad output: %s(%s)->%s(%s)" % (i, f, kf, t, kt))
    else:
        problems.append("edge %d bad role: %s" % (i, role))

if problems:
    print("VALIDATION FAILED (%d issues):" % len(problems))
    for p in problems:
        print("  - " + p)
    sys.exit(1)

# 3. max edge id
maxid = 0
for e in d["edges"]:
    try:
        maxid = max(maxid, int(str(e["id"]).split("_")[1]))
    except Exception:
        pass
nextid = maxid + 1

new_edges = []
for e in edges_raw:
    new_edges.append({
        "id": "e_%d" % nextid,
        "from": e["from"], "to": e["to"], "role": e["role"],
        "parameter_binding": {}, "used_in_theorem": e.get("used_in_theorem", ""),
    })
    nextid += 1

d["nodes"].extend(new_nodes)
d["edges"].extend(new_edges)

nid = [n["id"] for n in d["nodes"]]
assert len(nid) == len(set(nid)), "dup node ids after merge"
eid = [e["id"] for e in d["edges"]]
assert len(eid) == len(set(eid)), "dup edge ids after merge"

json.dump(d, open(GRAPH, "w"), ensure_ascii=False, indent=2)
print("OK nodes=%d edges=%d (added %d nodes, %d edges, edge ids %d..%d)" % (
    len(d["nodes"]), len(d["edges"]), len(new_nodes), len(new_edges), maxid + 1, nextid - 1))
