#!/usr/bin/env python3
"""
BANG - Self-built language model
Learns n-grams from memory.json and generates text from that only.
No external LLM.
"""

import json
import os
import sys
import random
import re
from collections import defaultdict

MEMORY_FILE = "memory.json"
MODEL_FILE = "lang_model.json"

def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    return [t for t in text.split() if t]

def extract_texts(mem):
    texts = []
    for v in mem.values():
        if isinstance(v, str):
            texts.append(v)
        elif isinstance(v, dict):
            for k in ("input", "response", "text", "value"):
                if k in v and isinstance(v[k], str):
                    texts.append(v[k])
            texts.append(json.dumps(v))
        else:
            texts.append(str(v))
    return texts

def train():
    if not os.path.exists(MEMORY_FILE):
        return {"bigrams": {}, "trigrams": {}, "vocab": [], "trained_on": 0}

    with open(MEMORY_FILE, "r") as f:
        mem = json.load(f)

    texts = extract_texts(mem)
    bigrams = defaultdict(lambda: defaultdict(int))
    trigrams = defaultdict(lambda: defaultdict(int))
    vocab = set()

    for text in texts:
        tokens = tokenize(text)
        vocab.update(tokens)
        for i in range(len(tokens) - 1):
            bigrams[tokens[i]][tokens[i + 1]] += 1
        for i in range(len(tokens) - 2):
            key = tokens[i] + " " + tokens[i + 1]
            trigrams[key][tokens[i + 2]] += 1

    model = {
        "bigrams": {k: dict(v) for k, v in bigrams.items()},
        "trigrams": {k: dict(v) for k, v in trigrams.items()},
        "vocab": sorted(vocab),
        "trained_on": len(texts)
    }
    with open(MODEL_FILE, "w") as f:
        json.dump(model, f)
    return model

def load_model():
    if os.path.exists(MODEL_FILE):
        with open(MODEL_FILE, "r") as f:
            return json.load(f)
    return train()

def sample_next(dist):
    if not dist:
        return None
    words, weights = zip(*dist.items())
    return random.choices(words, weights=weights, k=1)[0]

def generate(prompt="", max_words=25):
    model = load_model()
    tokens = tokenize(prompt) if prompt else []
    if not tokens:
        if not model["vocab"]:
            return "[lang_model]: No memory to speak from yet. Teach me more."
        tokens = [random.choice(model["vocab"])]

    output = list(tokens)
    for _ in range(max_words):
        next_word = None
        if len(output) >= 2:
            key = output[-2] + " " + output[-1]
            next_word = sample_next(model["trigrams"].get(key, {}))
        if not next_word:
            next_word = sample_next(model["bigrams"].get(output[-1], {}))
        if not next_word:
            break
        output.append(next_word)

    return " ".join(output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 lang_model.py [train|say <prompt>]")
        return
    cmd = sys.argv[1].lower()
    if cmd == "train":
        m = train()
        print(f"Trained on {m['trained_on']} memory texts. Vocab size: {len(m['vocab'])}")
    elif cmd == "say":
        prompt = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        print(generate(prompt))
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
