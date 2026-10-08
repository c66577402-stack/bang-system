#!/usr/bin/env python3
"""
BANG - Quantum-inspired graph dynamics (classical simulation)

Based on real QM–graph links:
- Superposition: node holds complex amplitude, not just real activation
- Quantum walk: unitary-like evolution on the graph (interference)
- Entanglement proxy: correlated amplitude pairs between nodes
- Measurement: collapse amplitudes to classical activation (Born rule)

This is NOT running on quantum hardware. It is a classical simulation
of quantum-inspired dynamics on the BANG graph.
"""

import json
import os
import sys
import math
import cmath
import random
from datetime import datetime

GRAPH_FILE = "graph_state.json"
QUANTUM_FILE = "quantum_state.json"

def load_graph():
    if os.path.exists(GRAPH_FILE):
        with open(GRAPH_FILE, "r") as f:
            return json.load(f)
    return {"nodes": {}, "edges": []}

def load_quantum():
    if os.path.exists(QUANTUM_FILE):
        with open(QUANTUM_FILE, "r") as f:
            return json.load(f)
    return {"amplitudes": {}, "entangled_pairs": [], "step": 0}

def save_quantum(q):
    with open(QUANTUM_FILE, "w") as f:
        json.dump(q, f, indent=2)

def _amp(q, node_id):
    """Get complex amplitude as (re, im)."""
    a = q["amplitudes"].get(node_id, {"re": 0.0, "im": 0.0})
    return complex(a.get("re", 0.0), a.get("im", 0.0))

def _set_amp(q, node_id, z):
    q["amplitudes"][node_id] = {"re": z.real, "im": z.imag}

def normalize(q, node_ids=None):
    """Normalize so total probability ~ 1 over selected nodes."""
    ids = node_ids or list(q["amplitudes"].keys())
    total = sum(abs(_amp(q, n)) ** 2 for n in ids) or 1e-12
    scale = 1.0 / math.sqrt(total)
    for n in ids:
        _set_amp(q, n, _amp(q, n) * scale)

def superpose(node_id, magnitude=1.0, phase_deg=0.0):
    """Put a node into superposition with given magnitude and phase."""
    q = load_quantum()
    g = load_graph()
    if node_id not in g.get("nodes", {}):
        # still allow orphan amplitudes
        pass
    phase = math.radians(phase_deg)
    z = magnitude * cmath.exp(1j * phase)
    _set_amp(q, node_id, z)
    normalize(q)
    save_quantum(q)
    return f"Superposition on {node_id}: |amp|={abs(z):.3f}, phase={phase_deg}°"

def entangle(a, b, strength=0.8):
    """Mark two nodes as entangled (correlated amplitudes)."""
    q = load_quantum()
    pair = tuple(sorted([a, b]))
    # store as list
    pairs = [tuple(p) if isinstance(p, list) else tuple(p) for p in q.get("entangled_pairs", [])]
    if pair not in pairs:
        q.setdefault("entangled_pairs", []).append(list(pair))
    # correlate: make b pick up phase-linked component from a
    za, zb = _amp(q, a), _amp(q, b)
    if abs(za) < 1e-9:
        za = complex(0.5, 0.0)
        _set_amp(q, a, za)
    zb = strength * za + (1 - strength) * zb
    _set_amp(q, b, zb)
    normalize(q)
    save_quantum(q)
    return f"Entangled {a} <-> {b} (strength={strength})"

def quantum_walk(steps=1, dt=0.3):
    """
    Continuous-time quantum-walk inspired evolution.
    Uses graph adjacency as Hamiltonian proxy:
      i dψ/dt = H ψ  (simulated with small steps)
    Interference emerges because amplitudes are complex.
    """
    q = load_quantum()
    g = load_graph()
    nodes = list(g.get("nodes", {}).keys())
    if not nodes:
        return "No graph nodes. Run: graph bootstrap"

    # ensure amplitudes exist
    for n in nodes:
        if n not in q["amplitudes"]:
            _set_amp(q, n, complex(0.0, 0.0))

    # build adjacency with weights
    adj = {n: [] for n in nodes}
    for e in g.get("edges", []):
        s, t = e["source"], e["target"]
        w = float(e.get("weight", 1.0))
        if s in adj and t in adj:
            adj[s].append((t, w))
            adj[t].append((s, w))  # undirected for walk

    for _ in range(steps):
        new = {}
        for n in nodes:
            # Hamiltonian term: sum over neighbors
            acc = complex(0.0, 0.0)
            for m, w in adj[n]:
                acc += w * _amp(q, m)
            # Euler step on i dψ/dt = -Hψ  => dψ = i * H * ψ * dt
            psi = _amp(q, n)
            dpsi = 1j * acc * dt
            new[n] = psi + dpsi
        for n, z in new.items():
            _set_amp(q, n, z)
        normalize(q, nodes)

        # enforce entanglement correlations lightly
        for pair in q.get("entangled_pairs", []):
            if len(pair) == 2 and pair[0] in nodes and pair[1] in nodes:
                a, b = pair[0], pair[1]
                za, zb = _amp(q, a), _amp(q, b)
                # pull toward phase alignment
                mid = 0.5 * (za + zb)
                _set_amp(q, a, 0.9 * za + 0.1 * mid)
                _set_amp(q, b, 0.9 * zb + 0.1 * mid)
        normalize(q, nodes)
        q["step"] = q.get("step", 0) + 1

    save_quantum(q)
    return f"Quantum walk: {steps} step(s) complete (total steps={q['step']})"

def measure(node_id=None):
    """
    Measurement / collapse using Born rule.
    Probability of node i = |amp_i|^2.
    Updates classical graph activation from outcome.
    """
    q = load_quantum()
    g = load_graph()
    amps = q.get("amplitudes", {})
    if not amps:
        return "No quantum amplitudes to measure."

    ids = list(amps.keys())
    probs = [abs(_amp(q, n)) ** 2 for n in ids]
    total = sum(probs) or 1e-12
    probs = [p / total for p in probs]

    if node_id and node_id in ids:
        # measure specific node: collapse toward observed/not
        p = abs(_amp(q, node_id)) ** 2 / total
        collapse_to = node_id if random.random() < p else None
    else:
        collapse_to = random.choices(ids, weights=probs, k=1)[0]

    # collapse: winner gets amplitude 1, others 0
    for n in ids:
        if n == collapse_to:
            _set_amp(q, n, complex(1.0, 0.0))
        else:
            _set_amp(q, n, complex(0.0, 0.0))

    # write classical activation
    if collapse_to and collapse_to in g.get("nodes", {}):
        g["nodes"][collapse_to]["activation"] = g["nodes"][collapse_to].get("activation", 0.0) + 1.0
        g["nodes"][collapse_to]["updated"] = datetime.now().isoformat()
        with open(GRAPH_FILE, "w") as f:
            json.dump(g, f, indent=2)

    save_quantum(q)
    return f"Measured → collapsed to: {collapse_to}"

def status():
    q = load_quantum()
    print("\n⚡ QUANTUM GRAPH STATUS")
    print("=" * 45)
    print(f"Walk steps: {q.get('step', 0)}")
    print(f"Entangled pairs: {len(q.get('entangled_pairs', []))}")
    print()
    amps = q.get("amplitudes", {})
    if not amps:
        print("No amplitudes. Try: qsuperpose seed")
    else:
        print(f"{'node':16} {'|amp|':>8} {'phase°':>8} {'prob':>8}")
        ranked = sorted(amps.keys(), key=lambda n: abs(_amp(q, n)), reverse=True)
        for n in ranked[:15]:
            z = _amp(q, n)
            print(f"{n:16} {abs(z):8.3f} {math.degrees(cmath.phase(z)):8.1f} {abs(z)**2:8.3f}")
    print("=" * 45)

def bootstrap_quantum():
    """Seed quantum state on trinity + entangle dark/light."""
    g = load_graph()
    if not g.get("nodes"):
        os.system("python3 graph.py bootstrap 2>/dev/null")
    superpose("seed", 0.7, 0)
    superpose("dark", 0.5, 45)
    superpose("light", 0.5, -45)
    entangle("dark", "light", 0.85)
    return "Quantum trinity bootstrapped (seed + entangled dark/light)"

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 quantum_graph.py status")
        print("  python3 quantum_graph.py bootstrap")
        print("  python3 quantum_graph.py superpose <node> [mag] [phase_deg]")
        print("  python3 quantum_graph.py entangle <a> <b> [strength]")
        print("  python3 quantum_graph.py walk [steps]")
        print("  python3 quantum_graph.py measure [node]")
        return

    cmd = sys.argv[1].lower()
    if cmd == "status":
        status()
    elif cmd == "bootstrap":
        print(bootstrap_quantum())
        status()
    elif cmd == "superpose":
        n = sys.argv[2]
        mag = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
        phase = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
        print(superpose(n, mag, phase))
    elif cmd == "entangle":
        a, b = sys.argv[2], sys.argv[3]
        s = float(sys.argv[4]) if len(sys.argv) > 4 else 0.8
        print(entangle(a, b, s))
    elif cmd == "walk":
        steps = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        print(quantum_walk(steps))
        status()
    elif cmd == "measure":
        node = sys.argv[2] if len(sys.argv) > 2 else None
        print(measure(node))
        status()
    else:
        print(f"Unknown: {cmd}")

if __name__ == "__main__":
    main()
