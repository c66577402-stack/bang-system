# BANG SYSTEM v2.2

Multi-agent intelligence framework with graph structure, Hebbian learning, autonomy, self-built language model, vector memory, and real fitness.

**No external LLM required.** Language comes from what the system has stored in its own memory.

---

## Layers

| Layer | File | Role |
|-------|------|------|
| Seed | bang.sh | Main interface + growth |
| Memory | memory.py | Perpetual store |
| Graph | graph.py | Nodes, edges, activation |
| Hebbian | hebbian.py | Trainable edge weights |
| Autonomy | autonomy.py | Background loop |
| Self LM | lang_model.py | N-gram model built from memory |
| Vectors | vector_memory.py | Semantic similarity search |
| Fitness | fitness.py | Task-based scoring |
| Swarm | swarm.py + workers | Darwinian multi-agent |
| Tools | tools.py | Search, export, improve |
| Creator | create_bot.py | Spawn new bot files |

---

## Quick start

```bash
git clone https://github.com/c66577402-stack/bang-system.git
cd bang-system
chmod +x bang.sh
./bang.sh
```

### Key new commands

```
hebbian              # strengthen co-active graph edges
autonomy 30          # background loop every 30s (Ctrl+C stop)
train                # rebuild self-built language model from memory
say hello world      # generate text from self-built LM
similar golden ratio # semantic search over memory
vectors              # rebuild vector index
fitness              # run real fitness evaluation
```

Default chat replies now use the **self-built language model** (trained on your memory).

---

## Docs

- `docs/EXPLAINED.md` — thorough explanation of the five upgrades
- `docs/MISSED.md` — remaining gaps
- `docs/ARCHITECTURE.md` — system map

---

## License
MIT
