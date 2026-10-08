# BANG Architecture v2.1

## Components

| Component     | File              | Role                                      |
|---------------|-------------------|-------------------------------------------|
| Seed          | bang.sh           | Main CLI + growth + command router        |
| Memory        | memory.py         | Perpetual JSON store + neural prototype   |
| Dark / Light  | bots/dark.py, light.py | Specialized halves                   |
| Workers       | bots/worker.py    | Swarm agents with fitness                 |
| Utility       | bots/utility.py   | Monitoring                                |
| Swarm Manager | swarm.py          | Spawn, Darwinian select, size limits      |
| Tools         | tools.py          | Search, run, export, import, improve      |
| Playground    | playground.py     | Multi-bot test mode                       |
| Creator       | create_bot.py     | Recursive new-bot generation              |
| **Graph**     | **graph.py**      | **Nodes, edges, activation, propagation** |

## Graph Layer

- **Nodes:** bots, concepts, system objects
- **Edges:** parent, influence, complement, manages, knows, monitors
- **Activation:** activity on a node spreads to neighbors by edge weight
- **Decay:** activations fade unless reinforced
- **Bootstrap:** builds the core Seed/Dark/Light/Swarm structure

This is still a lightweight graph (JSON-backed), not a trained neural net.  
It gives the system a real relational structure instead of only a flat memory file.

## Data files

- `memory.json` — shared knowledge
- `graph_state.json` — nodes + edges + activations
- `swarm_state.json` — worker list and limits
- `bang_state.txt` — Seed growth stats
