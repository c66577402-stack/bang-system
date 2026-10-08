#!/usr/bin/env python3
"""
BANG - Hebbian learning on the graph
When source and target are co-active, strengthen the edge.
"""

import json
import os
import sys
from datetime import datetime

GRAPH_FILE = "graph_state.json"

def load_graph():
    if os.path.exists(GRAPH_FILE):
        with open(GRAPH_FILE, "r") as f:
            return json.load(f)
    return {"nodes": {}, "edges": []}

def save_graph(g):
    with open(GRAPH_FILE, "w") as f:
        json.dump(g, f, indent=2)

def hebbian_update(lr=0.1, activity_threshold=0.1):
    """Strengthen edges between co-active nodes; slight decay otherwise."""
    g = load_graph()
    nodes = g.get("nodes", {})
    edges = g.get("edges", [])
    updated = 0

    for e in edges:
        src = nodes.get(e["source"], {})
        tgt = nodes.get(e["target"], {})
        a_src = src.get("activation", 0.0)
        a_tgt = tgt.get("activation", 0.0)

        if a_src >= activity_threshold and a_tgt >= activity_threshold:
            # fire together → wire together
            e["weight"] = min(5.0, float(e.get("weight", 1.0)) + lr * a_src * a_tgt)
            e["updated"] = datetime.now().isoformat()
            updated += 1
        else:
            # mild decay
            e["weight"] = max(0.05, float(e.get("weight", 1.0)) * 0.995)

    save_graph(g)
    return f"Hebbian update complete. Strengthened {updated} edges."

def main():
    lr = float(sys.argv[1]) if len(sys.argv) > 1 else 0.1
    print(hebbian_update(lr=lr))

if __name__ == "__main__":
    main()
