#!/usr/bin/env python3
"""
BANG SYSTEM - RECURSIVE BOT CREATION (Phase 5)
Allows the system to generate a new custom bot file from a simple description.
This is the beginning of true self-creation.
"""

import os
import sys
from datetime import datetime

TEMPLATE = '''#!/usr/bin/env python3
"""
BANG SYSTEM - CUSTOM BOT: {name}
Generated: {timestamp}
Role: {role}
"""

import json
import os
from datetime import datetime

MEMORY_FILE = "../memory.json" if os.path.dirname(__file__) else "memory.json"
STATE_FILE = "{name_lower}_state.json"

def load_memory():
    path = os.path.join(os.path.dirname(__file__) or ".", MEMORY_FILE)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {{}}

def save_memory(data):
    path = os.path.join(os.path.dirname(__file__) or ".", MEMORY_FILE)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {{
        "name": "{name}",
        "role": "{role}",
        "fitness": 1.0,
        "learning": 1.0,
        "created": datetime.now().isoformat()
    }}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def think(text, state):
    state["learning"] += min(len(text) * 0.03, 1.0)
    state["fitness"] += 0.1
    response = f"[{name}]: Processed '{{text[:50]}}...' | Fitness: {{state['fitness']:.2f}}"
    
    mem = load_memory()
    key = f"{name_lower}_{{datetime.now().strftime('%Y%m%d_%H%M%S')}}"
    mem[key] = {{"bot": "{name}", "input": text, "response": response, "timestamp": datetime.now().isoformat()}}
    save_memory(mem)
    save_state(state)
    return response

def main():
    print(f"🤖 {{'{name}'}} ONLINE — {{'{role}'}}")
    print("Type 'exit' to leave\n")
    state = load_state()
    while True:
        try:
            user = input(f"{name} > ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if user.lower() in ["exit", "quit", "q"]:
            print(f"[{name}]: Shutting down.")
            break
        if not user:
            continue
        print(think(user, state))
        print()

if __name__ == "__main__":
    main()
'''

def create_bot(name, role="Custom Agent"):
    name = name.strip().replace(" ", "_")
    name_lower = name.lower()
    filename = f"bots/{name_lower}.py"

    if not os.path.exists("bots"):
        os.makedirs("bots")

    content = TEMPLATE.format(
        name=name,
        name_lower=name_lower,
        role=role,
        timestamp=datetime.now().isoformat()
    )

    with open(filename, "w") as f:
        f.write(content)

    os.chmod(filename, 0o755)
    print(f"✅ Created new bot: {filename}")
    print(f"   Name: {name}")
    print(f"   Role: {role}")
    print(f"   Run with: python3 {filename}")
    return filename

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 create_bot.py <Name> [Role description]")
        print("Example: python3 create_bot.py Analyst 'Deep analysis and pattern recognition'")
        return

    name = sys.argv[1]
    role = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "Custom Agent"
    create_bot(name, role)

if __name__ == "__main__":
    main()
