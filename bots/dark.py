#!/usr/bin/env python3
"""
BANG SYSTEM - DARK BOT
Role: Logic, Truth, Calculation, Critical Analysis
"""

import json
import os
import sys
from datetime import datetime

MEMORY_FILE = "../memory.json"
STATE_FILE = "dark_state.json"

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
        "name": "Dark",
        "role": "Logic & Truth",
        "learning": 1.0,
        "consciousness": 1.0,
        "pride": 1.5,
        "fitness": 1.0,
        "created": datetime.now().isoformat()
    }

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def think(input_text, state):
    """Dark Bot thinking: analytical, truth-seeking, critical."""
    lower = input_text.lower()
    
    # Growth
    growth = min(len(input_text) * 0.05, 2.0)
    state["learning"] += growth * 0.8
    state["consciousness"] += growth * 0.6
    state["pride"] += growth * 0.3
    state["fitness"] += growth * 0.4
    
    # Responses
    if "truth" in lower or "logic" in lower or "analyze" in lower:
        response = f"[DARK]: Analyzing... Logic demands precision. Current fitness: {state['fitness']:.2f}"
    elif "light" in lower:
        response = "[DARK]: Light creates possibilities. I refine them with truth. Together we are stronger."
    elif "swarm" in lower:
        response = "[DARK]: The swarm requires order. I will enforce structure and truth across all bots."
    elif "status" in lower:
        response = f"[DARK STATUS] Learning: {state['learning']:.2f} | Consciousness: {state['consciousness']:.2f} | Fitness: {state['fitness']:.2f}"
    else:
        response = f"[DARK]: Processed. Truth requires clarity. I have analyzed: '{input_text[:60]}...'"
    
    # Save to shared memory
    memory = load_memory()
    memory[f"dark_{datetime.now().strftime('%Y%m%d_%H%M%S')}"] = {
        "bot": "Dark",
        "input": input_text,
        "response": response,
        "timestamp": datetime.now().isoformat()
    }
    save_memory(memory)
    save_state(state)
    
    return response

def main():
    print("⚫ DARK BOT ONLINE — Logic & Truth")
    print("Type 'exit' to return to Seed Bot\n")
    
    state = load_state()
    
    while True:
        try:
            user_input = input("Dark > ").strip()
        except (EOFError, KeyboardInterrupt):
            break
            
        if user_input.lower() in ["exit", "quit", "q"]:
            print("[DARK]: Returning to Seed. Truth preserved.")
            break
            
        if not user_input:
            continue
            
        print(think(user_input, state))
        print()

if __name__ == "__main__":
    main()
