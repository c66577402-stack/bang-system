# Quantum Mechanics and the BANG Graph

## Capacity of the system now (honest)

BANG operates at **prototype / research-architecture capacity**, not production AGI capacity.

| Capability | Level |
|------------|-------|
| Multi-agent structure | Working |
| Shared memory | Working (flat + vector) |
| Graph structure | Working |
| Hebbian learning | Working (simple) |
| Self-built language | Working but weak (n-grams) |
| Autonomy | Maintenance loop only |
| Quantum-inspired dynamics | Classical simulation |
| Real quantum hardware | None |
| Human-level reasoning | None |

It is a **complete structural framework** with many layers plugged together.  
It is **not** a high-capability intelligence by modern LLM standards.

---

## How quantum mechanics relates to graphs

Established research links:

1. **Quantum walks on graphs**  
   Quantum analogue of random walks. A walker in superposition explores many paths at once; interference amplifies or cancels paths. Used in quantum graph neural networks and graph classification.

2. **Superposition**  
   A node is not only "on/off" or a single activation — it holds a complex amplitude. Probability of finding activity there is |amplitude|² (Born rule).

3. **Interference**  
   Because amplitudes are complex, paths can constructively or destructively interfere. This is why quantum walks explore graphs differently from classical walks.

4. **Entanglement (proxy)**  
   Two nodes can share correlated state so measuring/affecting one constrains the other. In multi-agent terms: Dark and Light stay coupled.

5. **Measurement / collapse**  
   Looking at the system forces a definite classical outcome from the superposition, written back as ordinary graph activation.

---

## What we implemented (`quantum_graph.py`)

Classical simulation of the above on the BANG graph:

- `superpose` — complex amplitude on a node
- `entangle` — correlated pairs (e.g. dark <-> light)
- `walk` — quantum-walk-inspired evolution using edge weights as Hamiltonian proxy
- `measure` — Born-rule collapse into classical activation

**Important:** This runs on ordinary CPUs. It does not require a quantum computer. It borrows the *mathematics and structure* of QM for the agent graph.

---

## Commands

```bash
python3 quantum_graph.py bootstrap
python3 quantum_graph.py status
python3 quantum_graph.py walk 5
python3 quantum_graph.py measure
python3 quantum_graph.py superpose seed 1.0 0
python3 quantum_graph.py entangle dark light 0.9
```

Inside bang.sh (if wired): `qbootstrap`, `qwalk`, `qmeasure`, `qstatus`
