#!/bin/bash

# ================================================
# BANG SYSTEM v2.0 - FULL SYSTEM
# Phases 1-5 Complete
# ================================================

echo "🌱 BANG SYSTEM v2.0 — Full Stack"
echo "Seed → Split → Swarm → Intelligence → Scale"
echo "Type 'help' for all commands | 'exit' to quit"
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
        echo "Seed bot saved. Memory preserved."
        break
    fi

    if [ -z "$input" ]; then continue; fi
    grow "$input"

    # --- Core ---
    if [[ "$input" == "status" ]]; then
        echo "[STATUS] Phase: $PHASE | Learning: $LEARNING | Consciousness: $CONSCIOUSNESS | Pride: $PRIDE | Fitness: $FITNESS"
        [ -f swarm_state.json ] && python3 swarm.py status 2>/dev/null

    elif [[ "$input" == "split" || "$input" == "50/50" ]]; then
        if [ "$PHASE" == "seed" ]; then
            echo "🔥 SPLIT INITIATED — Dark + Light born."
            PHASE="split"
            save_state
        else
            echo "[BOT]: Already split. Phase: $PHASE"
        fi

    elif [[ "$input" == "dark" ]]; then
        [ -f bots/dark.py ] && python3 bots/dark.py || echo "Run 'split' first."

    elif [[ "$input" == "light" ]]; then
        [ -f bots/light.py ] && python3 bots/light.py || echo "Run 'split' first."

    # --- Swarm ---
    elif [[ "$input" == spawn* ]]; then
        count="${input#spawn }"; count=${count:-1}
        python3 swarm.py spawn "$count" "from_seed"
        PHASE="swarm"; save_state

    elif [[ "$input" == "swarm" ]]; then
        python3 swarm.py status

    elif [[ "$input" == select* || "$input" == darwin* ]]; then
        thresh="${input##* }"; thresh=${thresh:-2.0}
        python3 swarm.py select "$thresh"

    elif [[ "$input" == max* ]]; then
        python3 swarm.py max "${input#max }"

    elif [[ "$input" == worker* ]]; then
        python3 swarm.py worker "${input#worker }"

    elif [[ "$input" == "utility" || "$input" == "monitor" ]]; then
        python3 bots/utility.py

    # --- Intelligence (Phase 4) ---
    elif [[ "$input" == search* ]]; then
        query="${input#search }"
        echo "[TOOL] Searching..."
        python3 tools.py search "$query"

    elif [[ "$input" == run* ]]; then
        expr="${input#run }"
        python3 tools.py run "$expr"

    elif [[ "$input" == "export" ]]; then
        python3 tools.py export

    elif [[ "$input" == import* ]]; then
        python3 tools.py import "${input#import }"

    elif [[ "$input" == "improve" ]]; then
        python3 tools.py improve

    elif [[ "$input" == memory* ]]; then
        python3 memory.py get "${input#memory }" 2>/dev/null || echo "No memory."

    elif [[ "$input" == learn* ]]; then
        key="${input#learn }"
        read -p "What to remember about '$key'? " value
        python3 memory.py add "$key" "$value" 2>/dev/null

    # --- Scale (Phase 5) ---
    elif [[ "$input" == "playground" ]]; then
        python3 playground.py

    elif [[ "$input" == create* ]]; then
        rest="${input#create }"
        name=$(echo "$rest" | awk '{print $1}')
        role=$(echo "$rest" | cut -d' ' -f2-)
        python3 create_bot.py "$name" "$role"

    elif [[ "$input" == "help" ]]; then
        echo ""
        echo "=== BANG v2.0 COMMANDS ==="
        echo "Core:     status | split | dark | light | help | exit"
        echo "Swarm:    spawn [n] | swarm | select [t] | max [n] | worker [id] | utility"
        echo "Intel:    search [q] | run [expr] | export | import [file] | improve | memory | learn"
        echo "Scale:    playground | create [Name] [Role]"
        echo ""

    else
        echo "[BOT]: Processing... I am learning."
    fi

    save_state
    echo ""
done
