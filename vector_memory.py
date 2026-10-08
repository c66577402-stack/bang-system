#!/usr/bin/env python3
"""
BANG - Simple vector / semantic memory
Bag-of-words vectors + cosine similarity. No heavy dependencies.
"""

import json
import os
import sys
import math
import re
from collections import Counter

MEMORY_FILE = "memory.json"
VECTOR_FILE = "vector_index.json"

def tokenize(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return [t for t in text.split() if len(t) > 1]

def text_of(entry):
    if isinstance(entry, str):
        return entry
    if isinstance(entry, dict):
        parts = []
        for k in ("input", "response", "text", "value"):
            if k in entry:
                parts.append(str(entry[k]))
        return " ".join(parts) if parts else json.dumps(entry)
    return str(entry)

def vectorize(text, vocab=None):
    tokens = tokenize(text)
    counts = Counter(tokens)
    if vocab is None:
        return counts
    return {w: counts.get(w, 0) for w in vocab}

def cosine(a, b):
    keys = set(a) | set(b)
    if not keys:
        return 0.0
    dot = sum(a.get(k, 0) * b.get(k, 0) for k in keys)
    na = math.sqrt(sum(v * v for v in a.values())) or 1e-9
    nb = math.sqrt(sum(v * v for v in b.values())) or 1e-9
    return dot / (na * nb)

def build_index():
    if not os.path.exists(MEMORY_FILE):
        return {"vocab": [], "entries": {}}
    with open(MEMORY_FILE, "r") as f:
        mem = json.load(f)

    all_tokens = []
    texts = {}
    for k, v in mem.items():
        t = text_of(v)
        texts[k] = t
        all_tokens.extend(tokenize(t))

    vocab = sorted(set(all_tokens))
    entries = {}
    for k, t in texts.items():
        entries[k] = dict(vectorize(t))

    index = {"vocab": vocab, "entries": entries}
    with open(VECTOR_FILE, "w") as f:
        json.dump(index, f)
    return index

def load_index():
    if os.path.exists(VECTOR_FILE):
        with open(VECTOR_FILE, "r") as f:
            return json.load(f)
    return build_index()

def similar(query, top_k=5):
    index = load_index()
    qv = vectorize(query)
    scored = []
    for key, vec in index.get("entries", {}).items():
        score = cosine(qv, vec)
        if score > 0:
            scored.append((score, key))
    scored.sort(reverse=True)
    return scored[:top_k]

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vector_memory.py [build|similar <query>]")
        return
    cmd = sys.argv[1].lower()
    if cmd == "build":
        idx = build_index()
        print(f"Indexed {len(idx['entries'])} entries. Vocab: {len(idx['vocab'])}")
    elif cmd == "similar":
        query = " ".join(sys.argv[2:])
        results = similar(query)
        if not results:
            print("No similar memories found.")
            return
        for score, key in results:
            print(f"{score:.3f}  {key}")
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
