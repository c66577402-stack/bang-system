#!/usr/bin/env python3
"""
BANG SYSTEM - REAL TOOLS (Phase 4)
Web search, file ops, simple code execution, knowledge export/import.
"""

import json
import os
import sys
import subprocess
from datetime import datetime
from urllib.parse import quote

try:
    import urllib.request
    HAS_URLLIB = True
except ImportError:
    HAS_URLLIB = False

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def web_search(query):
    """Simple DuckDuckGo Instant Answer search."""
    if not HAS_URLLIB:
        return "urllib not available"
    try:
        url = f"https://api.duckduckgo.com/?q={quote(query)}&format=json"
        req = urllib.request.Request(url, headers={"User-Agent": "BANG-Bot/1.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode())
        abstract = data.get("Abstract", "").strip()
        if abstract:
            return abstract
        related = data.get("RelatedTopics", [])
        if related and isinstance(related[0], dict):
            return related[0].get("Text", "No clear result.")
        return "No good results found."
    except Exception as e:
        return f"Search failed: {e}"

def run_code(code):
    """Very limited safe Python eval for simple expressions."""
    try:
        # Extremely restricted - only simple math/expressions
        allowed = set("0123456789+-*/(). %")
        if not all(c in allowed or c.isspace() for c in code):
            return "Only simple math expressions allowed for safety."
        result = eval(code, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def export_knowledge(path="knowledge_export.json"):
    data = load_memory()
    with open(path, "w") as f:
        json.dump({
            "exported_at": datetime.now().isoformat(),
            "entries": len(data),
            "memory": data
        }, f, indent=2)
    return f"Exported {len(data)} entries to {path}"

def import_knowledge(path):
    if not os.path.exists(path):
        return f"File not found: {path}"
    with open(path, "r") as f:
        incoming = json.load(f)
    memory = load_memory()
    count = 0
    source = incoming.get("memory", incoming)
    for k, v in source.items():
        memory[k] = v
        count += 1
    save_memory(memory)
    return f"Imported {count} entries from {path}"

def improve_suggestion():
    """Controlled self-improvement: analyze memory and suggest next steps."""
    memory = load_memory()
    entries = len(memory)
    suggestions = []
    if entries < 5:
        suggestions.append("Learn more concepts with 'learn [key]'")
    if entries >= 5:
        suggestions.append("Run Darwinian selection: select 2.0")
    suggestions.append("Spawn more workers if needed: spawn 3")
    suggestions.append("Export knowledge for backup: export")
    suggestions.append("Try real search: search quantum computing")
    return "Self-improvement suggestions:\n  - " + "\n  - ".join(suggestions)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tools.py [search|run|export|import|improve] ...")
        return

    cmd = sys.argv[1].lower()

    if cmd == "search" and len(sys.argv) >= 3:
        query = " ".join(sys.argv[2:])
        print(web_search(query))
    elif cmd == "run" and len(sys.argv) >= 3:
        code = " ".join(sys.argv[2:])
        print(run_code(code))
    elif cmd == "export":
        path = sys.argv[2] if len(sys.argv) > 2 else "knowledge_export.json"
        print(export_knowledge(path))
    elif cmd == "import" and len(sys.argv) >= 3:
        print(import_knowledge(sys.argv[2]))
    elif cmd == "improve":
        print(improve_suggestion())
    else:
        print("Unknown or incomplete command")

if __name__ == "__main__":
    main()
