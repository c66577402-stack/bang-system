#!/usr/bin/env python3
"""
BANG SYSTEM - Memory + Neural Layer Module
Perpetual memory with Golden Ratio growth and basic neural processing.
"""

import json
import os
import sys

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_to_memory(key, value):
    data = load_memory()
    data[key] = value
    save_memory(data)
    return f"Memory updated: {key}"

def get_from_memory(key):
    data = load_memory()
    return data.get(key, "No memory found for that key.")

def list_memory():
    data = load_memory()
    if not data:
        return "Memory is empty."
    return "\n".join([f"- {k}: {str(v)[:80]}..." for k, v in data.items()])

# === NEURAL NETWORK LAYER (Prototype) ===
class NeuralLayer:
    def __init__(self, name, strength=1.0):
        self.name = name
        self.strength = strength
        self.connections = {}

    def connect(self, other_layer, weight=1.0):
        self.connections[other_layer.name] = weight

    def activate(self, input_value):
        return input_value * self.strength

# Basic 3-layer structure
input_layer = NeuralLayer("Input", 1.0)
hidden_layer = NeuralLayer("Hidden", 1.2)
output_layer = NeuralLayer("Output", 0.9)

input_layer.connect(hidden_layer, 0.8)
hidden_layer.connect(output_layer, 1.1)

def process_through_network(input_value):
    """Simple forward pass through the neural layers."""
    x = input_layer.activate(float(input_value))
    x = hidden_layer.activate(x)
    x = output_layer.activate(x)
    return x

# === CLI Interface for Bash ===
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 memory.py [get|add|list|neural] ...")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "get" and len(sys.argv) >= 3:
        print(get_from_memory(sys.argv[2]))
    elif cmd == "add" and len(sys.argv) >= 4:
        print(add_to_memory(sys.argv[2], " ".join(sys.argv[3:])))
    elif cmd == "list":
        print(list_memory())
    elif cmd == "neural" and len(sys.argv) >= 3:
        try:
            result = process_through_network(sys.argv[2])
            print(result)
        except ValueError:
            print("Error: neural expects a number")
    else:
        print("Unknown command or missing arguments")
