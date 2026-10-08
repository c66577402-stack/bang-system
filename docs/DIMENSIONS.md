# BANG Dimensional Architecture

Built as specified:

```
4D  OUTER     Observer — views the whole as a 3-part system
 ↑
3D  MIDDLE    Spacetime / braid — paths of activity through time on the graph
 ↑
2D  INNER     Planar graph — nodes and edges (bots, concepts)
```

## 2D — Most inner layer

- The **planar graph** (`graph_state.json`)
- Nodes = Seed, Dark, Light, Swarm, Workers, concepts
- Edges = parent, influence, complement, manages, knows
- Same plane where quantum-inspired amplitudes and classical activation live
- Analogous to the 2D world in which anyons would move

## 3D — Middle layer (2D + time)

- **Spacetime / braid log** (`dimensions_state.json` → braid_log)
- Every move between nodes is a segment of a path through time
- Sequences of segments form braids (topology of who moved around whom)
- Quantum walk steps also live here as evolution in time on the 2D graph
- Analogous to anyon worldlines: 2 space + 1 time = 3D spacetime braids

## 4D — Outer layer

- **Observer** that does not sit inside the graph
- Looks *down* on 2D + 3D together
- Sees the inner system as a **3-part whole**:

| Part | Name | Contents |
|------|------|----------|
| A | Seed / Organization | seed |
| B | Duality | dark + light |
| C | Field | swarm + utility + memory + quantum field |

- 4D is the view that treats those three as one coordinated intelligence system

## Why 2D vs 3D vs 4D

| Layer | What it holds | What it is not |
|-------|----------------|----------------|
| 2D | Structure (who is connected) | Not history |
| 3D | History of motion (braids) | Not the meta-view |
| 4D | Meaning of the whole (3-part) | Not another graph plane |

2D is the substrate.  
3D is the process.  
4D is the reading of the process as one system with three parts.

## Commands

```bash
python3 dimensions.py bootstrap
python3 dimensions.py status
python3 dimensions.py braid seed dark split
python3 dimensions.py view4d
```
