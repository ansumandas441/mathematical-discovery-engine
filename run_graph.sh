#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
PORT="${1:-8765}"

# Kill any existing server on the port
lsof -ti:"$PORT" | xargs kill -9 2>/dev/null || true

echo "Starting graph viewer on port $PORT..."
python3 -m http.server "$PORT" &>/dev/null &
SERVER_PID=$!
sleep 1

open "http://localhost:${PORT}/graph_viewer_3d.html"
echo "Opened 3D graph viewer at http://localhost:${PORT}/graph_viewer_3d.html"
echo "Server PID: $SERVER_PID — kill with: kill $SERVER_PID"
