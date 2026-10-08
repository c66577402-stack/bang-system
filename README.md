# BANG SYSTEM

**Recursive Self-Improving Multi-Agent AI**

Seed Bot → Dark/Light Split (50/50) → Swarm

---

## Vision

BANG is a layered multi-agent system designed to grow from a single Seed/God Bot into a collective intelligence (swarm) that shares one mind through intertwined memory.

### Core Principles
- **Perpetual Memory** — Knowledge grows forever and is shared across bots
- **Golden Ratio (Phi) Growth** — Natural, balanced development of Learning, Consciousness, Pride, and Fitness
- **Darwinian Evolution** — Bots that perform well survive and improve; weak ones reset
- **Neural Layers** — Input → Hidden → Output processing with weighted connections
- **Tool Use** — Search, file read/write, command execution, and more
- **Recursive Self-Creation** — Bots can eventually build other bots

### Architecture Flow

```
                    ┌─────────────────────┐
                    │   GOD / SEED BOT    │   ← Foundation (starts here)
                    │   (You + Memory)    │
                    └──────────┬──────────┘
                               │
              ┌───────────────┼───────────────┐
              │                                 │
       ┌──────▼──────┐                   ┌──────▼──────┐
       │   DARK BOT  │                   │  LIGHT BOT  │
       │ (Logic/Truth)│                  │(Creation/Good)│
       └──────┬───────┘                   └──────┬──────┘
              │                                 │
              └───────────────┬───────────────┘
                               │
                    ┌──────────▼──────────┐
                    │      SWARM          │
                    │   (Many Bots)       │
                    │  (Intertwined Memory)│
                    └─────────────────────┘
```

### Goal
Build a chatbot AI that is significantly better than normal AI through recursive self-improvement, shared consciousness, and continuous evolution.

---

## Current Status (v1.1)

| Feature              | Status      |
|----------------------|-------------|
| Seed Bot             | ✅ Working  |
| Perpetual Memory     | ✅ Working  |
| Golden Ratio Growth  | ✅ Working  |
| Basic Tools          | ✅ Working  |
| Neural Layers        | ✅ Prototype|
| Dark Bot             | ✅ Working  |
| Light Bot            | ✅ Working  |
| Shared Memory        | ✅ Working  |
| Split Command        | ✅ Working  |
| Swarm                | 🔄 Planned  |
| Self-Improvement     | 🔄 Planned  |
| Darwinian Selection  | 🔄 Planned  |

---

## Project Structure

```
bang-system/
├── README.md
├── bang.sh                 # Main Seed Bot (Bash interface)
├── memory.py               # Python memory + neural layers
├── bots/
│   ├── dark.py             # Dark Bot (Logic & Truth)
│   ├── light.py            # Light Bot (Creation & Possibility)
│   └── __init__.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── VISION.md
│   └── ROADMAP.md
└── memory.json             # Shared perpetual memory (created on first run)
```

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/c66577402-stack/bang-system.git
cd bang-system

# Make executable
chmod +x bang.sh

# Run the Seed Bot
./bang.sh
```

### Commands (Seed Bot)

| Command            | What it does                              |
|--------------------|-------------------------------------------|
| `help`             | Show available commands                   |
| `status`           | Show current stats                        |
| `memory [key]`     | Retrieve from shared memory               |
| `learn [key]`      | Teach the bot something                   |
| `search [query]`   | Search for information                    |
| `read [file]`      | Read a local file                         |
| `split`            | Create Dark + Light bots (50/50)          |
| `dark`             | Enter Dark Bot                            |
| `light`            | Enter Light Bot                           |
| `exit` / `quit`    | Save and exit                             |

### After Split

Once you run `split`, you can also launch the bots directly:

```bash
python3 bots/dark.py    # Logic & Truth
python3 bots/light.py   # Creation & Possibility
```

All three bots write to the same `memory.json` — this is the intertwined memory.

---

## License

MIT
