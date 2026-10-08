#!/bin/bash

# ================================================
# BANG SYSTEM v1.2 - SEED BOT + SPLIT + SWARM
# ================================================

echo "🌱 BANG SYSTEM v1.2 — Seed Bot + Swarm"
echo "Memory: Perpetual | Growth: Golden Ratio | Split: Ready | Swarm: Active"
echo "Type 'help' for commands | 'exit' to quit"
echo ""

MEMORY_FILE="memory.json"
STATE_FILE="bang_state.txt"

if [ ! -f "$MEMORY_FILE" ]; then
    echo "{}" > "$MEMORY_FILE"
fi

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

    if [[ "$input" == search* ]]; then
        query="${input#search }"
        echo "[TOOL] Searching: $query"
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
        if [ -f "swarm_state.json" ]; then
            python3 swarm.py status 2>/dev/null
        fi
    
    elif [[ "$input" == "split" || "$input" == "50/50" ]]; then
        if [ "$PHASE" == "seed" ]; then
            echo ""
            echo "🔥 SPLIT INITIATED"
            echo "Creating Dark Bot (Logic & Truth)..."
            echo "Creating Light Bot (Creation & Possibility)..."
            echo "✅ The 50/50 Trinity is born."
            echo ""
            echo "Commands: dark | light | spawn | swarm"
            PHASE="split"
            save_state
        else
            echo "[BOT]: Already split. Phase: $PHASE"
        fi
    
    elif [[ "$input" == "dark" ]]; then
        if [ -f "bots/dark.py" ]; then
            python3 bots/dark.py
        else
            echo "[BOT]: Dark Bot not found. Run 'split' first."
        fi
    
    elif [[ "$input" == "light" ]]; then
        if [ -f "bots/light.py" ]; then
            python3 bots/light.py
        else
            echo "[BOT]: Light Bot not found. Run 'split' first."
        fi
    
    # === SWARM COMMANDS ===
    elif [[ "$input" == spawn* ]]; then
        count="${input#spawn }"
        count=${count:-1}
        python3 swarm.py spawn "$count" "from_seed"
        PHASE="swarm"
        save_state
    
    elif [[ "$input" == "swarm" || "$input" == "swarm status" ]]; then
        python3 swarm.py status
    
    elif [[ "$input" == select* || "$input" == darwin* ]]; then
        threshold="${input#* }"
        threshold=${threshold:-2.0}
        python3 swarm.py select "$threshold"
    
    elif [[ "$input" == max* ]]; then
        num="${input#max }"
        python3 swarm.py max "$num"
    
    elif [[ "$input" == worker* ]]; then
        wid="${input#worker }"
        wid=${wid:-1}
        python3 swarm.py worker "$wid"
    
    elif [[ "$input" == "utility" || "$input" == "monitor" ]]; then
        python3 bots/utility.py
    
    elif [[ "$input" == "help" ]]; then
        echo "Commands:"
        echo "  status           - Show Seed + Swarm stats"
        echo "  split            - Create Dark + Light (50/50)"
        echo "  dark / light     - Enter Dark or Light Bot"
        echo "  spawn [n]        - Spawn n worker bots"
        echo "  swarm            - Show swarm status"
        echo "  select [thresh]  - Darwinian selection (reset weak bots)"
        echo "  max [n]          - Set max swarm size"
        echo "  worker [id]      - Enter a specific worker"
        echo "  utility          - Open monitoring bot"
        echo "  memory [key]     - Retrieve memory"
        echo "  learn [key]      - Teach something"
        echo "  help             - This help"
        echo "  exit             - Save and quit"
    
    else
        echo "[BOT]: Processing... I am learning from this."
    fi

    save_state
    echo ""
done
