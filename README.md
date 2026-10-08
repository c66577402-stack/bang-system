# BANG SYSTEM

**Recursive Self-Improving Multi-Agent AI**

Seed Bot → Dark/Light Split (50/50) → Swarm

---

## Vision

BANG is a layered multi-agent system designed to grow from a single Seed/God Bot into a collective intelligence (swarm) that shares one mind through intertwined memory.

### Core Principles
- **Perpetual Memory** — Knowledge grows forever and is shared across bots
- **Golden Ratio (Phi) Growth** — Natural, balanced development
- **Darwinian Evolution** — Strong bots survive; weak ones reset
- **Neural Layers** — Input → Hidden → Output processing
- **Tool Use** — Search, files, commands, monitoring
- **Recursive Self-Creation** — Bots can spawn other bots

### Architecture Flow

```
                    ┌─────────────────────┐
                    │   GOD / SEED BOT    │
                    └──────────┬──────────┘
                               │
              ┌───────────────┼───────────────┐
              │                                 │
       ┌──────▼──────┐                   ┌──────▼──────┐
       │   DARK BOT  │                   │  LIGHT BOT  │
       └──────┬───────┘                   └──────┬──────┘
              │                                 │
              └───────────────┬───────────────┘
                               │
                    ┌──────────▼──────────┐
                    │      SWARM          │
                    │  Workers + Utility  │
                    │  Darwinian Select   │
                    └─────────────────────┘
```

---

## Current Status (v1.2)

| Feature              | Status      |
|----------------------|-------------|
| Seed Bot             | ✅ Working  |
| Perpetual Memory     | ✅ Working  |
| Golden Ratio Growth  | ✅ Working  |
| Dark Bot             | ✅ Working  |
| Light Bot            | ✅ Working  |
| Shared Memory        | ✅ Working  |
| Worker Bots          | ✅ Working  |
| Swarm Manager        | ✅ Working  |
| Darwinian Selection  | ✅ Working  |
| Utility / Monitor    | ✅ Working  |
| Swarm Size Control   | ✅ Working  |
| Self-Improvement     | 🔄 Planned  |
| Real Web Tools       | 🔄 Planned  |

---

## Quick Start

```bash
git clone https://github.com/c66577402-stack/bang-system.git
cd bang-system
chmod +x bang.sh
./bang.sh
```

### Main Commands

| Command              | What it does                          |
|----------------------|---------------------------------------|
| `status`             | Seed + Swarm stats                    |
| `split`              | Create Dark + Light                   |
| `dark` / `light`     | Enter Dark or Light Bot               |
| `spawn [n]`          | Spawn n worker bots                   |
| `swarm`              | Show swarm status                     |
| `select [threshold]` | Darwinian selection (reset weak)      |
| `max [n]`            | Set max swarm size                    |
| `worker [id]`        | Enter a specific worker               |
| `utility`            | Open monitoring bot                   |
| `help`               | Full command list                     |
| `exit`               | Save and quit                         |

### Direct Swarm Control

```bash
python3 swarm.py status
python3 swarm.py spawn 5 "test"
python3 swarm.py select 2.0
python3 swarm.py max 30
python3 swarm.py worker 1
python3 bots/utility.py
```

---

## License

MIT
