#!/usr/bin/env python3
"""
BANG - Real fitness evaluation
Score bots/workers on simple measurable tasks.
"""

import json
import os
import sys
from datetime import datetime

MEMORY_FILE = "memory.json"
GRAPH_FILE = "graph_state.json"
SWARM_FILE = "swarm_state.json"
FITNESS_LOG = "fitness_log.json"

def load_json(path, default=None):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return default if default is not None else {}

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def task_memory_growth():
    mem = load_json(MEMORY_FILE, {})
    n = len(mem)
    # score 0-1 based on memory size (cap at 50 entries = full score)
    return min(1.0, n / 50.0), f"memory_entries={n}"

def task_graph_connectivity():
    g = load_json(GRAPH_FILE, {"nodes": {}, "edges": []})
    nodes = len(g.get("nodes", {}))
    edges = len(g.get("edges", []))
    if nodes == 0:
        return 0.0, "no_graph"
    density = edges / max(1, nodes * (nodes - 1))
    return min(1.0, density * 5), f"nodes={nodes},edges={edges}"

def task_swarm_health():
    swarm = load_json(SWARM_FILE, {"workers": []})
    workers = swarm.get("workers", [])
    if not workers:
        return 0.3, "no_workers"  # neutral if empty
    active = sum(1 for w in workers if w.get("status") == "active")
    avg_fit = sum(w.get("fitness", 1.0) for w in workers) / len(workers)
    score = 0.5 * (active / len(workers)) + 0.5 * min(1.0, avg_fit / 5.0)
    return score, f"active={active}/{len(workers)},avg_fit={avg_fit:.2f}"

def evaluate():
    results = {}
    s1, d1 = task_memory_growth()
    s2, d2 = task_graph_connectivity()
    s3, d3 = task_swarm_health()
    results["memory_growth"] = {"score": round(s1, 3), "detail": d1}
    results["graph_connectivity"] = {"score": round(s2, 3), "detail": d2}
    results["swarm_health"] = {"score": round(s3, 3), "detail": d3}
    overall = (s1 + s2 + s3) / 3.0
    results["overall"] = round(overall, 3)
    results["timestamp"] = datetime.now().isoformat()

    log = load_json(FITNESS_LOG, {"history": []})
    log.setdefault("history", []).append(results)
    log["history"] = log["history"][-50:]  # keep last 50
    log["latest"] = results
    save_json(FITNESS_LOG, log)

    # update swarm worker fitness with overall signal
    swarm = load_json(SWARM_FILE, {"workers": []})
    for w in swarm.get("workers", []):
        # blend existing fitness with system overall
        w["fitness"] = round(0.7 * w.get("fitness", 1.0) + 0.3 * (overall * 5), 3)
    save_json(SWARM_FILE, swarm)

    return results

def main():
    r = evaluate()
    print("\n📊 FITNESS EVALUATION")
    print("=" * 40)
    for k, v in r.items():
        if k in ("overall", "timestamp"):
            continue
        print(f"  {k}: {v['score']:.3f}  ({v['detail']})")
    print(f"\n  OVERALL: {r['overall']:.3f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
