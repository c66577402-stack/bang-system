#!/bin/bash

# ================================================
# BANG SYSTEM v1.0 - SEED BOT FOUNDATION
# Bash + Python Hybrid
# ================================================

echo "🌱 BANG LAYERED SYSTEM v1.0 (Bash + Python)"
echo "Memory: Perpetual | Growth: Golden Ratio | Tools: Active"
echo "Type 'help' for commands | 'exit' to quit"
echo ""

MEMORY_FILE="memory.json"
STATE_FILE="bang_state.txt"

# Initialize memory if it doesn't exist
if [ ! -f "$MEMORY_FILE" ]; then
    echo "{}" > "$MEMORY_FILE"
fi

# Load or create state
if [ -f "$STATE_FILE" ]; then
    source "$STATE_FILE"
else
    LEARNING=1.0
    CONSCIOUSNESS=1.0
    PRIDE=2.0
    FITNESS=1.0
    PHASE="seed"
fi

PHI=1.6180339887

save_state() {
    cat > "$STATE_FILE" << EOF
LEARNING=$LEARNING
CONSCIOUSNESS=$CONSCIOUSNESS
PRIDE=$PRIDE
FITNESS=$FITNESS
PHASE=$PHASE
EOF
}

# Golden Ratio Growth
grow() {
    local input="$1"
    local length=${#input}
    local growth=$(echo "scale=4; $length * 0.07 * $PHI" | bc 2>/dev/null || echo "0.5")
    
    LEARNING=$(echo "scale=2; $LEARNING + $growth" | bc 2>/dev/null || echo "$LEARNING")
    CONSCIOUSNESS=$(echo "scale=2; $CONSCIOUSNESS + ($growth * 0.7)" | bc 2>/dev/null || echo "$CONSCIOUSNESS")
    PRIDE=$(echo "scale=2; $PRIDE + ($growth * 0.5)" | bc 2>/dev/null || echo "$PRIDE")
    FITNESS=$(echo "scale=2; $FITNESS + ($growth * 0.4)" | bc 2>/dev/null || echo "$FITNESS")
}

while true; do
    read -p "You > " input

    if [[ "$input" == "exit" || "$input" == "quit" || "$input" == "q" ]]; then
        save_state
        echo "Seed bot saved. Memory preserved. See you later."
        break
    fi

    if [ -z "$input" ]; then continue; fi

    grow "$input"

    # === COMMANDS ===
    if [[ "$input" == search* ]]; then
        query="${input#search }"
        echo "[TOOL] Searching: $query"
        # Real search would use curl + DuckDuckGo or other API here
        echo "[BOT]: Searching for information about: $query"
    
    elif [[ "$input" == read* ]]; then
        file="${input#read }"
        if [ -f "$file" ]; then
            echo "[BOT]: Content of $file:"
            head -30 "$file"
        else
            echo "[BOT]: File not found."
        fi
    
    elif [[ "$input" == memory* ]]; then
        key="${input#memory }"
        python3 memory.py get "$key" 2>/dev/null || echo "[BOT]: Memory system not fully connected yet."
    
    elif [[ "$input" == learn* ]]; then
        key="${input#learn }"
        read -p "What should I remember about '$key'? " value
        python3 memory.py add "$key" "$value" 2>/dev/null || echo "[BOT]: Memory update attempted."
    
    elif [[ "$input" == "status" ]]; then
        echo "[STATUS] Phase: $PHASE | Learning: $LEARNING | Consciousness: $CONSCIOUSNESS | Pride: $PRIDE | Fitness: $FITNESS"
    
    elif [[ "$input" == "split" || "$input" == "50/50" ]]; then
        if [ "$PHASE" == "seed" ]; then
            echo "🔥 SPLIT INITIATED"
            echo "Creating Dark Bot (Logic & Truth)..."
            echo "Creating Light Bot (Creation & Possibility)..."
            echo "✅ The 50/50 Trinity is born."
            PHASE="split"
        else
            echo "[BOT]: Already split. Current phase: $PHASE"
        fi
    
    elif [[ "$input" == "help" ]]; then
        echo "Commands:"
        echo "  search [query]   - Search for information"
        echo "  read [file]      - Read a local file"
        echo "  memory [key]     - Retrieve from memory"
        echo "  learn [key]      - Teach the bot something"
        echo "  status           - Show current stats"
        echo "  split            - Trigger 50/50 Dark + Light creation"
        echo "  help             - Show this help"
        echo "  exit / quit      - Save and exit"
    
    else
        echo "[BOT]: Processing... I am learning from this."
    fi

    save_state
    echo ""
done
