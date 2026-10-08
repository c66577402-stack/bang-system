#!/usr/bin/env python3
"""
BANG - Autonomy loop
Runs periodic maintenance without user input each step.
Ctrl+C to stop.
"""

import json
import os
import sys
import time
from datetime import datetime

def run_once():
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Autonomy tick...")

    # 1. Decay graph activations
    if os.path.exists("graph.py"):
        os.system("python3 graph.py decay 0.92 2>/dev/null")

    # 2. Hebbian update
    if os.path.exists("hebbian.py"):
        os.system("python3 hebbian.py 0.08 2>/dev/null")

    # 3. Retrain self-built language model from memory
    if os.path.exists("lang_model.py"):
        os.system("python3 lang_model.py train 2>/dev/null")

    # 4. Rebuild vector index
    if os.path.exists("vector_memory.py"):
        os.system("python3 vector_memory.py build 2>/dev/null")

    # 5. Fitness evaluation
    if os.path.exists("fitness.py"):
        os.system("python3 fitness.py 2>/dev/null")

    # 6. Heartbeat into memory
    mem = {}
    if os.path.exists("memory.json"):
        with open("memory.json", "r") as f:
            mem = json.load(f)
    mem[f"heartbeat_{datetime.now().strftime('%Y%m%d_%H%M%S')}"] = {
        "event": "autonomy_tick",
        "timestamp": datetime.now().isoformat()
    }
    # keep memory from exploding
    if len(mem) > 500:
        keys = sorted(mem.keys())
        for k in keys[: len(mem) - 400]:
            if k.startswith("heartbeat_"):
                del mem[k]
    with open("memory.json", "w") as f:
        json.dump(mem, f, indent=2)

    print("  decay → hebbian → lang_train → vectors → fitness → heartbeat")

def main():
    interval = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    print("🔄 BANG AUTONOMY LOOP")
    print(f"Interval: {interval}s | Ctrl+C to stop\n")
    try:
        while True:
            run_once()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nAutonomy stopped.")

if __name__ == "__main__":
    main()
