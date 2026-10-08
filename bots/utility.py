#!/usr/bin/env python3
"""
BANG SYSTEM - UTILITY / MONITORING BOT
Watches system resources, swarm size, and overall health.
"""

import json
import os
import sys
from datetime import datetime

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

MEMORY_FILE = "../memory.json"
SWARM_FILE = "../swarm_state.json"

def load_memory():
    path = os.path.join(os.path.dirname(__file__), MEMORY_FILE)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def load_swarm():
    path = os.path.join(os.path.dirname(__file__), SWARM_FILE)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {"workers": [], "max_workers": 20, "created": datetime.now().isoformat()}

def get_system_stats():
    if not HAS_PSUTIL:
        return {
            "cpu": "psutil not installed",
            "memory": "psutil not installed",
            "note": "Run: pip install psutil"
        }
    return {
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "memory_percent": psutil.virtual_memory().percent,
        "memory_used_gb": round(psutil.virtual_memory().used / (1024**3), 2),
        "memory_total_gb": round(psutil.virtual_memory().total / (1024**3), 2)
    }

def report():
    swarm = load_swarm()
    memory = load_memory()
    stats = get_system_stats()

    print("🛠 UTILITY BOT — SYSTEM REPORT")
    print("=" * 40)
    print(f"Swarm workers: {len(swarm.get('workers', []))}")
    print(f"Max workers:   {swarm.get('max_workers', 20)}")
    print(f"Memory entries: {len(memory)}")
    print()
    print("Hardware:")
    if isinstance(stats.get("cpu_percent"), (int, float)):
        print(f"  CPU:    {stats['cpu_percent']}%")
        print(f"  RAM:    {stats['memory_percent']}% ({stats['memory_used_gb']} / {stats['memory_total_gb']} GB)")
    else:
        print(f"  {stats.get('note', 'No hardware stats available')}")
    print()

    # List active workers
    workers = swarm.get("workers", [])
    if workers:
        print("Active Workers:")
        for w in workers:
            print(f"  - {w.get('name', w.get('id'))} | Fitness: {w.get('fitness', 0):.2f} | Status: {w.get('status', 'unknown')}")
    else:
        print("No workers spawned yet.")
    print("=" * 40)

def main():
    print("🛠 UTILITY BOT ONLINE — Monitoring")
    print("Commands: report, status, exit\n")

    while True:
        try:
            user_input = input("Utility > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break

        if user_input in ["exit", "quit", "q"]:
            print("[UTILITY]: Monitoring paused.")
            break
        elif user_input in ["report", "status", ""]:
            report()
        else:
            print("[UTILITY]: Commands: report, status, exit")

if __name__ == "__main__":
    main()
