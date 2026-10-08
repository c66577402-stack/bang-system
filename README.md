# BANG SYSTEM v2.1

**Recursive Self-Improving Multi-Agent AI + Graph Layer**

Seed → Dark/Light → Swarm → Intelligence → Scale → **Graph**

---

## What it is

A multi-agent framework where bots share one mind (memory), specialize (Dark/Light), scale (swarm), select (Darwinian), create new bots, use tools, and are now connected through a **graph** of nodes and edges.

---

## Architecture

```
SEED ─────────── Dark
  │   parent/influence     │
  │                        complement
  └────────────── Light
  │
  └─ controls ─ Swarm ─ manages ─ Workers
                    │
                    └ monitors ─ Utility
```

Graph nodes = bots + concepts.  
Edges = parent, influence, complement, manages, knows, etc.  
Activation propagates along edges.

---

## Status

| Layer            | Status     |
|------------------|------------|
| Seed + Memory    | ✅         |
| Dark / Light     | ✅         |
| Swarm + Darwin   | ✅         |
| Tools + Improve  | ✅         |
| Playground       | ✅         |
| Bot Creation     | ✅         |
| **Graph Layer**  | ✅ New     |

---

## Quick Start

```bash
git clone https://github.com/c66577402-stack/bang-system.git
cd bang-system
chmod +x bang.sh
pip install -r requirements.txt   # optional
./bang.sh
```

### Important new commands

```
graph                 # show graph status
graph bootstrap       # create Seed/Dark/Light structure
activate seed 1.0     # activate a node + propagate
decay                 # decay all activations
```

### Full command groups
- **Core:** status, split, dark, light, exit
- **Swarm:** spawn, swarm, select, max, worker, utility
- **Intel:** search, run, export, import, improve, memory, learn
- **Scale:** playground, create [Name] [Role]
- **Graph:** graph, graph bootstrap, activate, decay

---

## Direct graph usage

```bash
python3 graph.py bootstrap
python3 graph.py status
python3 graph.py activate seed 1.5
python3 graph.py add_edge dark light complement 0.9
python3 graph.py neighbors seed
python3 graph.py decay 0.9
```

---

## License
MIT
