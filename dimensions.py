#!/usr/bin/env python3
"""
BANG Dimensional Architecture

2D (inner)  = planar graph of nodes/edges (bots, concepts)
3D          = spacetime: graph + time (paths, braids, walk history)
4D (outer)  = observer layer viewing the inner system as a 3-part whole

3-part system (seen from 4D):
  Part A = Seed / Organization
  Part B = Dark+Light / Duality
  Part C = Swarm+Memory+Quantum / Field
"""

import json
import os
import sys
from datetime import datetime

GRAPH_FILE = "graph_state.json"
QUANTUM_FILE = "quantum_state.json"
MEMORY_FILE = "memory.json"
SWARM_FILE = "swarm_state.json"
DIM_FILE = "dimensions_state.json"

def load_json(path, default=None):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return default if default is not None else {}

def save_dim(d):
    with open(DIM_FILE, "w") as f:
        json.dump(d, f, indent=2)

def load_dim():
    d = load_json(DIM_FILE, None)
    if d:
        return d
    return {
        "version": "1.0",
        "layers": {
            "2d": {"name": "Inner Graph", "role": "planar nodes and edges"},
            "3d": {"name": "Spacetime / Braid", "role": "paths through time on the graph"},
            "4d": {"name": "Outer Observer", "role": "views full system as 3-part whole"}
        },
        "three_part": {
            "A_seed": {"label": "Seed / Organization", "nodes": ["seed"]},
            "B_duality": {"label": "Dark + Light", "nodes": ["dark", "light"]},
            "C_field": {"label": "Swarm + Memory + Quantum", "nodes": ["swarm", "utility"]}
        },
        "braid_log": [],
        "created": datetime.now().isoformat()
    }

# ---------- 2D: inner planar graph ----------
def layer_2d_status():
    g = load_json(GRAPH_FILE, {"nodes": {}, "edges": []})
    return {
        "layer": "2D",
        "description": "Inner planar graph — most inner layer",
        "nodes": len(g.get("nodes", {})),
        "edges": len(g.get("edges", {})),
        "node_ids": list(g.get("nodes", {}).keys())[:20]
    }

# ---------- 3D: spacetime / braid (graph + time) ----------
def braid(source, target, label="move"):
    """Record a path in spacetime: a segment of a braid on the 2D graph over time."""
    d = load_dim()
    entry = {
        "from": source,
        "to": target,
        "label": label,
        "t": datetime.now().isoformat()
    }
    d.setdefault("braid_log", []).append(entry)
    d["braid_log"] = d["braid_log"][-200:]
    save_dim(d)
    return f"3D braid segment: {source} → {target} ({label})"

def layer_3d_status():
    d = load_dim()
    log = d.get("braid_log", [])
    q = load_json(QUANTUM_FILE, {})
    return {
        "layer": "3D",
        "description": "Spacetime / braid layer — paths of activity through time",
        "braid_segments": len(log),
        "recent": log[-5:],
        "quantum_steps": q.get("step", 0)
    }

# ---------- 4D: outer observer of 3-part system ----------
def layer_4d_view():
    """Outer layer: see the whole inner system as three parts."""
    g = load_json(GRAPH_FILE, {"nodes": {}, "edges": []})
    mem = load_json(MEMORY_FILE, {})
    swarm = load_json(SWARM_FILE, {"workers": []})
    q = load_json(QUANTUM_FILE, {})
    d = load_dim()

    nodes = g.get("nodes", {})
    parts = d.get("three_part", {})

    def part_activation(node_list):
        total = 0.0
        for n in node_list:
            if n in nodes:
                total += float(nodes[n].get("activation", 0))
            # quantum probability mass
            amp = q.get("amplitudes", {}).get(n, {})
            re, im = amp.get("re", 0), amp.get("im", 0)
            total += (re * re + im * im)
        return total

    view = {
        "layer": "4D",
        "description": "Outer observer — views 2D+3D as one 3-part system",
        "parts": {}
    }
    for key, info in parts.items():
        view["parts"][key] = {
            "label": info["label"],
            "nodes": info["nodes"],
            "activation_mass": round(part_activation(info["nodes"]), 4)
        }

    view["totals"] = {
        "memory_entries": len(mem),
        "graph_nodes": len(nodes),
        "workers": len(swarm.get("workers", [])),
        "braid_segments": len(d.get("braid_log", [])),
        "quantum_steps": q.get("step", 0)
    }
    return view

def status():
    print("\n🌌 DIMENSIONAL ARCHITECTURE")
    print("=" * 50)
    s2 = layer_2d_status()
    print(f"2D INNER  (graph):     {s2['nodes']} nodes, {s2['edges']} edges")
    s3 = layer_3d_status()
    print(f"3D MIDDLE (spacetime): {s3['braid_segments']} braid segments, qsteps={s3['quantum_steps']}")
    s4 = layer_4d_view()
    print(f"4D OUTER  (observer):  views system as 3 parts")
    print()
    print("3-part system (from 4D):")
    for k, p in s4["parts"].items():
        print(f"  {p['label']}: nodes={p['nodes']}  mass={p['activation_mass']}")
    print()
    print("Totals:", s4["totals"])
    print("=" * 50)

def bootstrap_dimensions():
    d = load_dim()
    save_dim(d)
    # ensure core graph exists
    if not load_json(GRAPH_FILE, {}).get("nodes"):
        os.system("python3 graph.py bootstrap 2>/dev/null")
    # seed a few braid segments as structure
    braid("seed", "dark", "split")
    braid("seed", "light", "split")
    braid("dark", "light", "complement")
    braid("seed", "swarm", "controls")
    return "Dimensional stack initialized (2D inner / 3D braid / 4D observer + 3-part view)"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 dimensions.py [status|bootstrap|braid <from> <to> [label]|view4d]")
        return
    cmd = sys.argv[1].lower()
    if cmd == "status":
        status()
    elif cmd == "bootstrap":
        print(bootstrap_dimensions())
        status()
    elif cmd == "braid":
        a, b = sys.argv[2], sys.argv[3]
        label = sys.argv[4] if len(sys.argv) > 4 else "move"
        print(braid(a, b, label))
    elif cmd == "view4d":
        v = layer_4d_view()
        print(json.dumps(v, indent=2))
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
