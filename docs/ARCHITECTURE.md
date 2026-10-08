# BANG System Architecture

## Layered Design

| Layer     | Language | Responsibility                          |
|-----------|----------|-----------------------------------------|
| Interface | Bash     | User interaction, command parsing, state |
| Memory    | Python   | Perpetual knowledge store, neural layers |
| Mind      | Rust (planned) | Heavy computation, tools, self-improvement |

## Core Components

### 1. Seed / God Bot
- Single starting agent
- Holds the primary memory and growth state
- Can trigger the 50/50 split

### 2. Dark + Light (50/50 Split)
- Dark: Logic, Truth, Calculation
- Light: Creation, Possibility, Exploration
- Together they form the Trinity with the Seed

### 3. Swarm
- Many worker bots created from the Trinity
- Share intertwined memory (one mind)
- Darwinian selection: strong bots survive, weak ones reset

### 4. Memory System
- `memory.json` — persistent key-value store
- Grows forever (perpetual)
- Accessible by all bots

### 5. Growth Engine
- Uses Golden Ratio (φ ≈ 1.618) for balanced growth
- Tracks: Learning, Consciousness, Pride, Fitness

### 6. Neural Layers (Prototype)
- Input → Hidden → Output
- Weighted connections
- Foundation for deeper reasoning

## Communication Model
All bots communicate through the shared memory file.  
This creates the "one mind" effect across the swarm.
