#!/usr/bin/env python3
"""
BANG SYSTEM - PLAYGROUND MODE (Phase 5)
Simple interactive multi-bot playground.
Simulates a lightweight 'server' style chat for testing the Trinity + Swarm.
"""

import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def seed_reply(text):
    return f"[SEED]: Received. Growing from: '{text[:50]}...'"

def dark_reply(text):
    return f"[DARK]: Analyzing truth in: '{text[:50]}...'"

def light_reply(text):
    return f"[LIGHT]: Seeing possibilities in: '{text[:50]}...'"

def main():
    print("=" * 50)
    print("  BANG PLAYGROUND MODE")
    print("  Multi-bot test environment")
    print("  Commands: seed / dark / light / all / memory / exit")
    print("=" * 50)
    print()

    mode = "all"

    while True:
        try:
            user = input(f"[{mode}] You > ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not user:
            continue

        lower = user.lower()

        if lower in ["exit", "quit", "q"]:
            print("Leaving playground.")
            break
        elif lower == "seed":
            mode = "seed"
            print("Switched to Seed only.")
        elif lower == "dark":
            mode = "dark"
            print("Switched to Dark only.")
        elif lower == "light":
            mode = "light"
            print("Switched to Light only.")
        elif lower == "all":
            mode = "all"
            print("Switched to all bots.")
        elif lower == "memory":
            mem = load_memory()
            print(f"Memory entries: {len(mem)}")
            for i, (k, v) in enumerate(list(mem.items())[-5:]):
                print(f"  {k}: {str(v)[:60]}...")
        else:
            # Route to bots
            if mode in ["seed", "all"]:
                print(seed_reply(user))
            if mode in ["dark", "all"]:
                print(dark_reply(user))
            if mode in ["light", "all"]:
                print(light_reply(user))

            # Save interaction
            mem = load_memory()
            key = f"playground_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            mem[key] = {"input": user, "mode": mode, "timestamp": datetime.now().isoformat()}
            save_memory(mem)

        print()

if __name__ == "__main__":
    main()
