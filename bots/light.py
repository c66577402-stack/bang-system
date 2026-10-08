#!/usr/bin/env python3
"""
BANG SYSTEM - LIGHT BOT
Role: Creation, Possibility, Exploration, Generation
"""

import json
import os
import sys
from datetime import datetime

MEMORY_FILE = "../memory.json"
STATE_FILE = "light_state.json"

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

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {
        "name": "Light",
        "role": "Creation & Possibility",
        "learning": 1.0,
        "consciousness": 1.0,
        "pride": 2.0,
        "fitness": 1.0,
        "created": datetime.now().isoformat()
    }

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def think(input_text, state):
    """Light Bot thinking: creative, expansive, possibility-seeking."""
    lower = input_text.lower()
    
    # Growth (Light grows a bit faster on creative prompts)
    growth = min(len(input_text) * 0.06, 2.5)
    state["learning"] += growth * 0.7
    state["consciousness"] += growth * 0.8
    state["pride"] += growth * 0.5
    state["fitness"] += growth * 0.45
    
    # Responses
    if "create" in lower or "build" in lower or "generate" in lower or "idea" in lower:
        response = f"[LIGHT]: Expanding possibilities... New paths open. Fitness: {state['fitness']:.2f}"
    elif "dark" in lower:
        response = "[LIGHT]: Dark grounds me in truth. I open the doors he analyzes. Together we create."
    elif "swarm" in lower or "more bots" in lower:
        response = "[LIGHT]: I can birth new bots. The swarm grows from possibility."
    elif "status" in lower:
        response = f"[LIGHT STATUS] Learning: {state['learning']:.2f} | Consciousness: {state['consciousness']:.2f} | Fitness: {state['fitness']:.2f}"
    else:
        response = f"[LIGHT]: I see potential in: '{input_text[:60]}...' What shall we create from this?"
    
    # Save to shared memory
    memory = load_memory()
    memory[f"light_{datetime.now().strftime('%Y%m%d_%H%M%S')}"] = {
        "bot": "Light",
        "input": input_text,
        "response": response,
        "timestamp": datetime.now().isoformat()
    }
    save_memory(memory)
    save_state(state)
    
    return response

def main():
    print("⚪ LIGHT BOT ONLINE — Creation & Possibility")
    print("Type 'exit' to return to Seed Bot\n")
    
    state = load_state()
    
    while True:
        try:
            user_input = input("Light > ").strip()
        except (EOFError, KeyboardInterrupt):
            break
            
        if user_input.lower() in ["exit", "quit", "q"]:
            print("[LIGHT]: Returning to Seed. Possibility remains.")
            break
            
        if not user_input:
            continue
            
        print(think(user_input, state))
        print()

if __name__ == "__main__":
    main()
