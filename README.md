# BANG SYSTEM v2.0

**Recursive Self-Improving Multi-Agent AI**

Seed → Dark/Light (50/50) → Swarm → Intelligence → Scale

**All 5 phases complete.**

---

## Architecture

```
SEED BOT (bang.sh)
    ├─ Dark Bot      (Logic & Truth)
    ├─ Light Bot     (Creation & Possibility)
    ├─ Swarm Manager (spawn, select, max)
    │     ├─ Worker Bots (fitness + Darwinian reset)
    │     └─ Utility Bot (monitoring)
    ├─ Tools         (search, run, export, improve)
    ├─ Playground    (multi-bot test mode)
    └─ create_bot    (recursive bot generation)
```

All bots share one mind through `memory.json`.

---

## Status

| Phase | Feature                        | Status     |
|-------|--------------------------------|------------|
| 1     | Seed Bot + Memory + Growth     | ✅ Complete |
| 2     | Dark + Light Split             | ✅ Complete |
| 3     | Swarm + Darwinian + Utility    | ✅ Complete |
| 4     | Tools + Self-Improve + Export  | ✅ Complete |
| 5     | Playground + Create Bot + Cloud| ✅ Complete |

---

## Quick Start

```bash
git clone https://github.com/c66577402-stack/bang-system.git
cd bang-system
chmod +x bang.sh
pip install -r requirements.txt   # optional (for utility monitoring)
./bang.sh
```

### Full Command List

**Core**
- `status` — Show stats
- `split` — Birth Dark + Light
- `dark` / `light` — Enter those bots
- `exit` — Save and quit

**Swarm**
- `spawn [n]` — Create workers
- `swarm` — Swarm status
- `select [threshold]` — Darwinian reset of weak bots
- `max [n]` — Limit swarm size
- `worker [id]` — Enter a worker
- `utility` — System monitor

**Intelligence**
- `search [query]` — Real web search
- `run [expression]` — Simple math/code
- `export` — Backup knowledge
- `import [file]` — Load knowledge
- `improve` — Self-improvement suggestions
- `memory [key]` / `learn [key]` — Memory ops

**Scale**
- `playground` — Multi-bot test environment
- `create [Name] [Role]` — Generate a brand new bot

---

## Direct Scripts

```bash
python3 swarm.py status
python3 swarm.py spawn 5
python3 tools.py search "golden ratio"
python3 tools.py improve
python3 playground.py
python3 create_bot.py Analyst "Deep analysis"
python3 bots/utility.py
```

---

## License

MIT
