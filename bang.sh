#!/bin/bash
# BANG v2.3 — includes quantum-inspired graph layer

echo "🌱 BANG SYSTEM v2.3 — Quantum-inspired graph active"
echo "Type 'help' | 'exit'"
echo ""

MEMORY_FILE="memory.json"
STATE_FILE="bang_state.txt"
[ ! -f "$MEMORY_FILE" ] && echo "{}" > "$MEMORY_FILE"
if [ -f "$STATE_FILE" ]; then source "$STATE_FILE"
else LEARNING=1.0; CONSCIOUSNESS=1.0; PRIDE=2.0; FITNESS=1.0; PHASE="seed"; fi
PHI=1.6180339887
save_state() { cat > "$STATE_FILE" << EOF
LEARNING=$LEARNING
CONSCIOUSNESS=$CONSCIOUSNESS
PRIDE=$PRIDE
FITNESS=$FITNESS
PHASE=$PHASE
EOF
}
grow() {
  local length=${#1}
  local growth=$(echo "scale=4; $length * 0.07 * $PHI" | bc 2>/dev/null || echo "0.5")
  LEARNING=$(echo "scale=2; $LEARNING + $growth" | bc 2>/dev/null || echo "$LEARNING")
  CONSCIOUSNESS=$(echo "scale=2; $CONSCIOUSNESS + ($growth * 0.7)" | bc 2>/dev/null || echo "$CONSCIOUSNESS")
  PRIDE=$(echo "scale=2; $PRIDE + ($growth * 0.5)" | bc 2>/dev/null || echo "$PRIDE")
  FITNESS=$(echo "scale=2; $FITNESS + ($growth * 0.4)" | bc 2>/dev/null || echo "$FITNESS")
}

while true; do
  read -p "You > " input
  [[ "$input" == "exit" || "$input" == "quit" || "$input" == "q" ]] && { save_state; echo "Saved."; break; }
  [ -z "$input" ] && continue
  grow "$input"

  if [[ "$input" == "status" ]]; then
    echo "[STATUS] Phase:$PHASE L:$LEARNING C:$CONSCIOUSNESS P:$PRIDE F:$FITNESS"
    [ -f swarm_state.json ] && python3 swarm.py status 2>/dev/null
    [ -f graph_state.json ] && python3 graph.py status 2>/dev/null
    [ -f quantum_state.json ] && python3 quantum_graph.py status 2>/dev/null
  elif [[ "$input" == "split" || "$input" == "50/50" ]]; then
    [[ "$PHASE" == "seed" ]] && { echo "🔥 SPLIT"; PHASE="split"; python3 graph.py bootstrap 2>/dev/null; python3 quantum_graph.py bootstrap 2>/dev/null; } || echo "Already split"
  elif [[ "$input" == "dark" ]]; then python3 bots/dark.py 2>/dev/null || echo "split first"
  elif [[ "$input" == "light" ]]; then python3 bots/light.py 2>/dev/null || echo "split first"
  elif [[ "$input" == spawn* ]]; then c="${input#spawn }"; c=${c:-1}; python3 swarm.py spawn "$c" from_seed; PHASE="swarm"
  elif [[ "$input" == "swarm" ]]; then python3 swarm.py status
  elif [[ "$input" == select* ]]; then python3 swarm.py select "${input##* }"
  elif [[ "$input" == max* ]]; then python3 swarm.py max "${input#max }"
  elif [[ "$input" == worker* ]]; then python3 swarm.py worker "${input#worker }"
  elif [[ "$input" == "utility" ]]; then python3 bots/utility.py
  elif [[ "$input" == search* ]]; then python3 tools.py search "${input#search }"
  elif [[ "$input" == run* ]]; then python3 tools.py run "${input#run }"
  elif [[ "$input" == "export" ]]; then python3 tools.py export
  elif [[ "$input" == import* ]]; then python3 tools.py import "${input#import }"
  elif [[ "$input" == "improve" ]]; then python3 tools.py improve
  elif [[ "$input" == memory* ]]; then python3 memory.py get "${input#memory }" 2>/dev/null
  elif [[ "$input" == learn* ]]; then
    key="${input#learn }"; read -p "Value for $key? " value
    python3 memory.py add "$key" "$value" 2>/dev/null
    python3 lang_model.py train 2>/dev/null; python3 vector_memory.py build 2>/dev/null
  elif [[ "$input" == "playground" ]]; then python3 playground.py
  elif [[ "$input" == create* ]]; then
    rest="${input#create }"; name=$(echo "$rest"|awk '{print $1}'); role=$(echo "$rest"|cut -d' ' -f2-)
    python3 create_bot.py "$name" "$role"
  elif [[ "$input" == "graph"* ]]; then
    [[ "$input" == "graph bootstrap" ]] && python3 graph.py bootstrap || python3 graph.py status
  elif [[ "$input" == activate* ]]; then
    rest="${input#activate }"; n=$(echo "$rest"|awk '{print $1}'); a=$(echo "$rest"|awk '{print $2}'); a=${a:-1}
    python3 graph.py activate "$n" "$a"; python3 hebbian.py 2>/dev/null
  elif [[ "$input" == "decay" ]]; then python3 graph.py decay
  elif [[ "$input" == "hebbian" ]]; then python3 hebbian.py
  elif [[ "$input" == "autonomy"* ]]; then sec="${input#autonomy }"; sec=${sec:-30}; python3 autonomy.py "$sec"
  elif [[ "$input" == "train" ]]; then python3 lang_model.py train
  elif [[ "$input" == say* ]]; then python3 lang_model.py say "${input#say }"
  elif [[ "$input" == similar* ]]; then python3 vector_memory.py similar "${input#similar }"
  elif [[ "$input" == "vectors" ]]; then python3 vector_memory.py build
  elif [[ "$input" == "fitness" ]]; then python3 fitness.py
  # Quantum
  elif [[ "$input" == "qstatus" || "$input" == "quantum" ]]; then python3 quantum_graph.py status
  elif [[ "$input" == "qbootstrap" ]]; then python3 quantum_graph.py bootstrap
  elif [[ "$input" == qwalk* ]]; then steps="${input#qwalk }"; steps=${steps:-3}; python3 quantum_graph.py walk "$steps"
  elif [[ "$input" == "qmeasure" ]]; then python3 quantum_graph.py measure
  elif [[ "$input" == qsuperpose* ]]; then
    rest="${input#qsuperpose }"; n=$(echo "$rest"|awk '{print $1}'); m=$(echo "$rest"|awk '{print $2}'); p=$(echo "$rest"|awk '{print $3}')
    python3 quantum_graph.py superpose "$n" "${m:-1}" "${p:-0}"
  elif [[ "$input" == qentangle* ]]; then
    rest="${input#qentangle }"; a=$(echo "$rest"|awk '{print $1}'); b=$(echo "$rest"|awk '{print $2}'); s=$(echo "$rest"|awk '{print $3}')
    python3 quantum_graph.py entangle "$a" "$b" "${s:-0.8}"
  elif [[ "$input" == "help" ]]; then
    echo "Core: status split dark light exit"
    echo "Swarm: spawn swarm select max worker utility"
    echo "Intel: search run export import improve memory learn train say similar vectors fitness"
    echo "Graph: graph | activate | decay | hebbian"
    echo "Auto:  autonomy [sec]"
    echo "Quantum: qbootstrap | qstatus | qwalk [n] | qmeasure | qsuperpose [node] [mag] [phase] | qentangle [a] [b]"
  else
    echo "[BOT]: $(python3 lang_model.py say "$input" 2>/dev/null || echo Processing...)"
    python3 graph.py activate seed 0.2 2>/dev/null
  fi
  save_state; echo ""
done
