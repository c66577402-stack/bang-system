#!/usr/bin/env python3
"""
BANG SYSTEM - SWARM MANAGER
Handles spawning workers, Darwinian selection, and swarm control.
"""

import json
import os
import sys
from datetime import datetime

SWARM_FILE = "swarm_state.json"
MEMORY_FILE = "memory.json"
MAX_DEFAULT = 20

def load_swarm():
    if os.path.exists(SWARM_FILE):
        with open(SWARM_FILE, "r") as f:
            return json.load(f)
    return {
        "workers": [],
        "max_workers": MAX_DEFAULT,
        "total_spawned": 0,
        "total_reset": 0,
        "created": datetime.now().isoformat()
    }

def save_swarm(swarm):
    with open(SWARM_FILE, "w") as f:
        json.dump(swarm, f, indent=2)

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def spawn(count=1, reason="manual"):
    swarm = load_swarm()
    current = len(swarm["workers"])
    max_w = swarm.get("max_workers", MAX_DEFAULT)

    if current >= max_w:
        print(f"[SWARM]: Max workers reached ({max_w}). Cannot spawn more.")
        return

    spawned = 0
    for _ in range(count):
        if len(swarm["workers"]) >= max_w:
            break

        swarm["total_spawned"] += 1
        worker_id = str(swarm["total_spawned"])
        worker = {
            "id": worker_id,
            "name": f"Worker-{worker_id}",
            "fitness": 1.0,
            "status": "active",
            "created": datetime.now().isoformat(),
            "reason": reason
        }
        swarm["workers"].append(worker)
        spawned += 1

        # Log to shared memory
        memory = load_memory()
        memory[f"spawn_{worker_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"] = {
            "event": "spawn",
            "worker": worker["name"],
            "reason": reason,
            "timestamp": datetime.now().isoformat()
        }
        save_memory(memory)

    save_swarm(swarm)
    print(f"[SWARM]: Spawned {spawned} worker(s). Total active: {len(swarm['workers'])}")

def darwinian_select(threshold=2.0):
    """Reset workers with low fitness. Keep strong ones."""
    swarm = load_swarm()
    kept = []
    reset_count = 0

    for w in swarm["workers"]:
        if w.get("fitness", 1.0) < threshold:
            # Reset this worker
            w["fitness"] = 1.0
            w["status"] = "reset"
            w["reset_at"] = datetime.now().isoformat()
            swarm["total_reset"] = swarm.get("total_reset", 0) + 1
            reset_count += 1
            print(f"  → {w['name']} reset (fitness was low)")
        else:
            w["status"] = "active"
            kept.append(w)
            print(f"  → {w['name']} survived (fitness: {w.get('fitness', 0):.2f})")

    # Keep reset workers but mark them (or remove if preferred)
    # For now we keep them after reset so the swarm size stays stable
    swarm["workers"] = swarm["workers"]  # already updated in place
    save_swarm(swarm)

    print(f"\n[SWARM]: Darwinian selection complete. Reset: {reset_count} | Active: {len(swarm['workers'])}")

def set_max(n):
    swarm = load_swarm()
    swarm["max_workers"] = int(n)
    save_swarm(swarm)
    print(f"[SWARM]: Max workers set to {n}")

def status():
    swarm = load_swarm()
    print("\n🐝 SWARM STATUS")
    print("=" * 40)
    print(f"Active workers: {len(swarm.get('workers', []))}")
    print(f"Max workers:    {swarm.get('max_workers', MAX_DEFAULT)}")
    print(f"Total spawned:  {swarm.get('total_spawned', 0)}")
    print(f"Total reset:    {swarm.get('total_reset', 0)}")
    print()
    for w in swarm.get("workers", []):
        print(f"  {w['name']:12} | Fitness: {w.get('fitness', 0):.2f} | Status: {w.get('status', '?')}")
    print("=" * 40)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 swarm.py status")
        print("  python3 swarm.py spawn [count] [reason]")
        print("  python3 swarm.py select [threshold]")
        print("  python3 swarm.py max [number]")
        print("  python3 swarm.py worker [id]   # launch a worker")
        return

    cmd = sys.argv[1].lower()

    if cmd == "status":
        status()
    elif cmd == "spawn":
        count = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        reason = sys.argv[3] if len(sys.argv) > 3 else "manual"
        spawn(count, reason)
    elif cmd == "select":
        threshold = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
        print("[SWARM]: Running Darwinian selection...")
        darwinian_select(threshold)
    elif cmd == "max":
        if len(sys.argv) < 3:
            print("Usage: python3 swarm.py max [number]")
            return
        set_max(sys.argv[2])
    elif cmd == "worker":
        worker_id = sys.argv[2] if len(sys.argv) > 2 else "1"
        os.system(f"python3 bots/worker.py {worker_id}")
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
