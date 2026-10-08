# BANG System Architecture

## Layered Design

| Layer     | Language | Responsibility                          |
|-----------|----------|-----------------------------------------|
| Interface | Bash     | User interaction, command parsing, state |
| Memory    | Python   | Perpetual knowledge store, neural layers |
| Bots      | Python   | Dark (Logic) + Light (Creation)         |
| Mind      | Rust (planned) | Heavy computation, tools, self-improvement |

## Core Components

### 1. Seed / God Bot (`bang.sh`)
- Single starting agent
- Holds the primary growth state (Learning, Consciousness, Pride, Fitness)
- Can trigger the 50/50 split
- Launches Dark and Light bots

### 2. Dark Bot (`bots/dark.py`)
- Role: Logic, Truth, Calculation, Critical Analysis
- Writes to shared `memory.json`
- Grows with analytical prompts

### 3. Light Bot (`bots/light.py`)
- Role: Creation, Possibility, Exploration, Generation
- Writes to shared `memory.json`
- Grows faster on creative prompts

### 4. Shared Memory (`memory.json`)
- Persistent key-value store
- All bots read from and write to the same file
- This creates the "one mind" / intertwined memory effect

### 5. Growth Engine
- Uses Golden Ratio (φ ≈ 1.618) for balanced growth
- Tracks: Learning, Consciousness, Pride, Fitness

### 6. Neural Layers (Prototype in `memory.py`)
- Input → Hidden → Output
- Weighted connections
- Foundation for deeper reasoning

## Communication Model
All bots communicate through the shared `memory.json` file.  
This creates the "one mind" effect across the swarm.

When Dark or Light processes something, it is saved with a timestamped key.  
Any bot can later read the full memory and build on what the others have learned.
