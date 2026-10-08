#!/usr/bin/env python3
"""
BANG SYSTEM - WORKER BOT
Generic swarm worker. Created by the Trinity.
Has fitness score. Can be reset by Darwinian selection.
"""

import json
import os
import sys
from datetime import datetime

MEMORY_FILE = "../memory.json"

def load_memory():
    path = os.path.join(os.path.dirname(__file__), MEMORY_FILE)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    path = os.path.join(os.path.dirname(__file__), MEMORY_FILE)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_worker_state(worker_id):
    state_file = f"worker_{worker_id}_state.json"
    if os.path.exists(state_file):
        with open(state_file, "r") as f:
            return json.load(f)
    return {
        "id": worker_id,
        "name": f"Worker-{worker_id}",
        "role": "Swarm Worker",
        "fitness": 1.0,
        "learning": 0.5,
        "tasks_completed": 0,
        "created": datetime.now().isoformat(),
        "status": "active"
    }

def save_worker_state(state):
    state_file = f"worker_{state['id']}_state.json"
    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)

def think(input_text, state):
    lower = input_text.lower()
    growth = min(len(input_text) * 0.04, 1.5)
    state["learning"] += growth
    state["fitness"] += growth * 0.3
    state["tasks_completed"] += 1

    if "task" in lower or "do" in lower or "work" in lower:
        response = f"[{state['name']}]: Task accepted. Fitness now {state['fitness']:.2f}"
    elif "status" in lower:
        response = f"[{state['name']}] Fitness: {state['fitness']:.2f} | Tasks: {state['tasks_completed']} | Status: {state['status']}"
    elif "reset" in lower:
        state["fitness"] = 1.0
        state["learning"] = 0.5
        state["status"] = "reset"
        response = f"[{state['name']}]: Reset complete. Starting fresh."
    else:
        response = f"[{state['name']}]: Processed. Learning: {state['learning']:.2f}"

    # Write to shared memory
    memory = load_memory()
    key = f"worker_{state['id']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    memory[key] = {
        "bot": state["name"],
        "input": input_text,
        "response": response,
        "fitness": state["fitness"],
        "timestamp": datetime.now().isoformat()
    }
    save_memory(memory)
    save_worker_state(state)
    return response

def main():
    worker_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    state = load_worker_state(worker_id)

    print(f"🐝 {state['name']} ONLINE — Swarm Worker")
    print(f"Fitness: {state['fitness']:.2f} | Type 'exit' to leave\n")

    while True:
        try:
            user_input = input(f"{state['name']} > ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if user_input.lower() in ["exit", "quit", "q"]:
            print(f"[{state['name']}]: Returning to swarm.")
            break

        if not user_input:
            continue

        print(think(user_input, state))
        print()

if __name__ == "__main__":
    main()
