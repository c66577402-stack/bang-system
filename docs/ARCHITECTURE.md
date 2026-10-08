# BANG System Architecture

## Layered Design

| Layer     | Language | Responsibility                          |
|-----------|----------|-----------------------------------------|
| Interface | Bash     | User interaction, command parsing       |
| Memory    | Python   | Perpetual knowledge store, neural layers|
| Trinity   | Python   | Seed + Dark + Light                     |
| Swarm     | Python   | Workers, Darwinian selection, Utility   |
| Mind      | Rust (planned) | Heavy computation, advanced tools |

## Core Components

### 1. Seed / God Bot (`bang.sh`)
- Primary interface
- Triggers split and swarm commands
- Holds growth state (Learning, Consciousness, Pride, Fitness)

### 2. Dark Bot (`bots/dark.py`)
- Logic, Truth, Calculation
- Writes to shared memory

### 3. Light Bot (`bots/light.py`)
- Creation, Possibility, Exploration
- Writes to shared memory

### 4. Worker Bots (`bots/worker.py`)
- Generic swarm agents
- Have fitness scores
- Can be reset by Darwinian selection
- All write to the same memory.json

### 5. Swarm Manager (`swarm.py`)
- `spawn [n]` — Create workers
- `select [threshold]` — Darwinian selection
- `max [n]` — Limit swarm size
- `status` — Overview
- `worker [id]` — Launch specific worker

### 6. Utility Bot (`bots/utility.py`)
- Monitors swarm size
- Reports system resources (CPU/RAM if psutil available)
- Health overview

### 7. Shared Memory (`memory.json`)
- All bots read/write the same file
- Creates the "one mind" effect

## Darwinian Selection
Workers below a fitness threshold are reset (fitness returns to 1.0).  
Strong workers keep their progress.  
This is the beginning of natural selection inside the swarm.
