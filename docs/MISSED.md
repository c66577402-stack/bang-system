# What Was Missed or Skipped

Audit after adding the graph layer.

## Implemented now
- Multi-agent structure (Seed, Dark, Light, Workers)
- Shared perpetual memory
- Golden Ratio growth stats
- Darwinian selection on workers
- Swarm spawn / size control
- Utility monitoring
- Basic tools (search, export, import, improve)
- Playground mode
- Recursive bot file creation
- **Graph of nodes/edges with activation propagation**

## Still missing (important)

1. **Real neural network learning**
   - Graph exists, but weights do not train from experience.
   - No backpropagation or Hebbian-style update beyond manual activation.

2. **Continuous autonomy**
   - System still waits for user commands.
   - No background loop that sets goals and acts on its own.

3. **Strong reasoning engine**
   - Bots use simple rule responses.
   - No deep language understanding unless wired to an external LLM.

4. **Rich memory**
   - Flat JSON only.
   - No embeddings, semantic search, or long-term structured knowledge graph beyond the new graph.py layer.

5. **Real fitness evaluation**
   - Fitness is mostly a counter, not measured success on hard tasks.

6. **Safe self-modification**
   - create_bot writes new files, but the system cannot yet rewrite its own core logic safely.

7. **Multi-process / multi-machine**
   - Everything is local single-folder.
   - No networked swarm.

8. **UI / external interfaces**
   - Terminal only (+ playground).
   - No web UI, Discord, or API server.

## Priority order if continuing
1. Trainable graph weights (even simple Hebbian)
2. Autonomy loop
3. Optional LLM tool for real language
4. Vector memory
5. Better fitness metrics
