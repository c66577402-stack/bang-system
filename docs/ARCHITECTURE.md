# BANG System Architecture v2.0

## Full Stack

| Component        | File                  | Role                                      |
|------------------|-----------------------|-------------------------------------------|
| Seed Interface   | `bang.sh`             | Main CLI, growth, command router          |
| Memory           | `memory.py`           | Perpetual JSON memory + neural layers     |
| Dark Bot         | `bots/dark.py`        | Logic & Truth                             |
| Light Bot        | `bots/light.py`       | Creation & Possibility                    |
| Worker Bots      | `bots/worker.py`      | Swarm agents with fitness                 |
| Utility Bot      | `bots/utility.py`     | Monitoring + resource report              |
| Swarm Manager    | `swarm.py`            | Spawn, Darwinian select, size control     |
| Tools            | `tools.py`            | Search, run, export, import, improve      |
| Playground       | `playground.py`       | Multi-bot interactive test mode           |
| Bot Creator      | `create_bot.py`       | Recursive generation of new bots          |
| Cloud Notes      | `docs/CLOUD.md`       | Deployment guidance                       |

## Data Flow

All bots → read/write `memory.json` → one shared mind.

Seed controls growth stats in `bang_state.txt`.  
Swarm state lives in `swarm_state.json`.  
Individual workers keep light local state files.

## Design Philosophy

- Start with one Seed
- Split into complementary halves (Dark/Light)
- Scale into a swarm under Darwinian pressure
- Add real tools and self-reflection
- Allow the system to create new bots of its own
