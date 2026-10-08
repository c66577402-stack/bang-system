#!/usr/bin/env python3
"""
BANG SYSTEM - GRAPH LAYER
Nodes = bots / concepts / memory keys
Edges = influence, parent, communication, knowledge links
Supports propagation of activity across the graph.
"""

import json
import os
import sys
from datetime import datetime
from collections import defaultdict

GRAPH_FILE = "graph_state.json"
MEMORY_FILE = "memory.json"

def load_graph():
    if os.path.exists(GRAPH_FILE):
        with open(GRAPH_FILE, "r") as f:
            return json.load(f)
    return {
        "nodes": {},
        "edges": [],
        "created": datetime.now().isoformat(),
        "version": "1.0"
    }

def save_graph(g):
    with open(GRAPH_FILE, "w") as f:
        json.dump(g, f, indent=2)

def add_node(node_id, node_type="bot", label=None, data=None):
    g = load_graph()
    if node_id in g["nodes"]:
        # update existing
        g["nodes"][node_id]["updated"] = datetime.now().isoformat()
        if data:
            g["nodes"][node_id]["data"].update(data)
        save_graph(g)
        return f"Updated node: {node_id}"

    g["nodes"][node_id] = {
        "id": node_id,
        "type": node_type,
        "label": label or node_id,
        "data": data or {},
        "activation": 0.0,
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat()
    }
    save_graph(g)
    return f"Added node: {node_id} ({node_type})"

def add_edge(source, target, relation="influence", weight=1.0):
    g = load_graph()
    if source not in g["nodes"]:
        add_node(source)
        g = load_graph()
    if target not in g["nodes"]:
        add_node(target)
        g = load_graph()

    # avoid exact duplicates
    for e in g["edges"]:
        if e["source"] == source and e["target"] == target and e["relation"] == relation:
            e["weight"] = weight
            e["updated"] = datetime.now().isoformat()
            save_graph(g)
            return f"Updated edge: {source} -[{relation}]-> {target} (w={weight})"

    g["edges"].append({
        "source": source,
        "target": target,
        "relation": relation,
        "weight": float(weight),
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat()
    })
    save_graph(g)
    return f"Added edge: {source} -[{relation}]-> {target} (w={weight})"

def get_neighbors(node_id, direction="out"):
    g = load_graph()
    result = []
    for e in g["edges"]:
        if direction == "out" and e["source"] == node_id:
            result.append(e)
        elif direction == "in" and e["target"] == node_id:
            result.append(e)
        elif direction == "both" and (e["source"] == node_id or e["target"] == node_id):
            result.append(e)
    return result

def activate(node_id, amount=1.0):
    """Raise activation on a node and propagate along outgoing edges."""
    g = load_graph()
    if node_id not in g["nodes"]:
        add_node(node_id)
        g = load_graph()

    g["nodes"][node_id]["activation"] = g["nodes"][node_id].get("activation", 0.0) + amount
    g["nodes"][node_id]["updated"] = datetime.now().isoformat()

    # simple one-step propagation
    propagated = []
    for e in g["edges"]:
        if e["source"] == node_id:
            target = e["target"]
            if target in g["nodes"]:
                delta = amount * float(e.get("weight", 1.0)) * 0.5
                g["nodes"][target]["activation"] = g["nodes"][target].get("activation", 0.0) + delta
                g["nodes"][target]["updated"] = datetime.now().isoformat()
                propagated.append((target, delta))

    save_graph(g)
    return {
        "activated": node_id,
        "amount": amount,
        "propagated": propagated
    }

def decay(factor=0.9):
    """Decay all activations (forgets over time unless reinforced)."""
    g = load_graph()
    for nid, node in g["nodes"].items():
        node["activation"] = node.get("activation", 0.0) * factor
    save_graph(g)
    return "Activations decayed"

def status():
    g = load_graph()
    nodes = g.get("nodes", {})
    edges = g.get("edges", [])
    print("\n🔗 GRAPH STATUS")
    print("=" * 45)
    print(f"Nodes: {len(nodes)}")
    print(f"Edges: {len(edges)}")
    print()
    if nodes:
        print("Top activated nodes:")
        ranked = sorted(nodes.values(), key=lambda n: n.get("activation", 0), reverse=True)[:10]
        for n in ranked:
            print(f"  {n['id']:20} type={n.get('type','?'):10} act={n.get('activation',0):.3f}")
    print()
    if edges:
        print("Recent edges:")
        for e in edges[-8:]:
            print(f"  {e['source']} -[{e['relation']} w={e['weight']}]-> {e['target']}")
    print("=" * 45)

def bootstrap_trinity():
    """Create the core Seed/Dark/Light graph structure."""
    add_node("seed", "bot", "Seed/God Bot")
    add_node("dark", "bot", "Dark Bot - Logic & Truth")
    add_node("light", "bot", "Light Bot - Creation & Possibility")
    add_node("swarm", "system", "Swarm Manager")
    add_node("utility", "bot", "Utility / Monitor")

    add_edge("seed", "dark", "parent", 1.0)
    add_edge("seed", "light", "parent", 1.0)
    add_edge("dark", "seed", "influence", 0.8)
    add_edge("light", "seed", "influence", 0.8)
    add_edge("dark", "light", "complement", 0.9)
    add_edge("light", "dark", "complement", 0.9)
    add_edge("seed", "swarm", "controls", 1.0)
    add_edge("swarm", "utility", "monitors", 0.7)

    # link existing memory keys as concept nodes if any
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            mem = json.load(f)
        for i, key in enumerate(list(mem.keys())[:20]):
            cid = f"mem_{i}"
            add_node(cid, "concept", key[:40], {"memory_key": key})
            add_edge("seed", cid, "knows", 0.5)

    return "Trinity graph bootstrapped"

def link_worker(worker_id):
    wid = f"worker_{worker_id}"
    add_node(wid, "bot", f"Worker-{worker_id}")
    add_edge("swarm", wid, "manages", 1.0)
    add_edge("seed", wid, "parent", 0.6)
    return f"Worker {worker_id} linked into graph"

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 graph.py status")
        print("  python3 graph.py bootstrap")
        print("  python3 graph.py add_node <id> [type] [label]")
        print("  python3 graph.py add_edge <source> <target> [relation] [weight]")
        print("  python3 graph.py activate <id> [amount]")
        print("  python3 graph.py decay [factor]")
        print("  python3 graph.py neighbors <id>")
        print("  python3 graph.py link_worker <id>")
        return

    cmd = sys.argv[1].lower()

    if cmd == "status":
        status()
    elif cmd == "bootstrap":
        print(bootstrap_trinity())
        status()
    elif cmd == "add_node":
        nid = sys.argv[2]
        ntype = sys.argv[3] if len(sys.argv) > 3 else "bot"
        label = sys.argv[4] if len(sys.argv) > 4 else nid
        print(add_node(nid, ntype, label))
    elif cmd == "add_edge":
        src, tgt = sys.argv[2], sys.argv[3]
        rel = sys.argv[4] if len(sys.argv) > 4 else "influence"
        w = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
        print(add_edge(src, tgt, rel, w))
    elif cmd == "activate":
        nid = sys.argv[2]
        amt = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
        result = activate(nid, amt)
        print(f"Activated {result['activated']} += {result['amount']}")
        for t, d in result["propagated"]:
            print(f"  → propagated to {t} (+{d:.3f})")
    elif cmd == "decay":
        factor = float(sys.argv[2]) if len(sys.argv) > 2 else 0.9
        print(decay(factor))
    elif cmd == "neighbors":
        nid = sys.argv[2]
        for e in get_neighbors(nid, "both"):
            print(f"{e['source']} -[{e['relation']} w={e['weight']}]-> {e['target']}")
    elif cmd == "link_worker":
        print(link_worker(sys.argv[2]))
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
