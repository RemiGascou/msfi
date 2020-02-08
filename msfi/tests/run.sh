#!/usr/bin/env bash

echo "[LOG] Starting nc localhost 2234"
e(){ echo -e "\x1b[4mmsf5 >\x1b[0m\n\x1b[4mmsf5\x1b[0m test(\x1b[91mLalla\x1b[0m) >\x1b[0m\n\x1b[4mmsf5 > new\x1b[0m\n" | timeout 10 nc -lvp 2234 2>&1 >/dev/null; }
e 2>&1 >/dev/null &

echo "[LOG] Running python3 explist.py"
python3 explist.py
