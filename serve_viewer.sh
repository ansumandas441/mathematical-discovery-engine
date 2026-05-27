#!/usr/bin/env bash
# Start a local HTTP server in this directory and open the graph viewer.
# Usage: ./serve_viewer.sh [port]
# Default port: 8765

set -e
cd "$(dirname "$0")"
PORT="${1:-8765}"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 not found. Install Python 3 or run any static file server here."
  exit 1
fi

URL="http://localhost:${PORT}/graph_viewer.html"
echo "Serving $(pwd) on port ${PORT}"
echo "Viewer:  ${URL}"
echo "JSON:    http://localhost:${PORT}/knowledge_graph.json"
echo "Press Ctrl+C to stop."

# Open the viewer in the default browser (macOS; Linux users can swap to xdg-open)
if command -v open >/dev/null 2>&1; then
  (sleep 1 && open "${URL}") &
elif command -v xdg-open >/dev/null 2>&1; then
  (sleep 1 && xdg-open "${URL}") &
fi

exec python3 -m http.server "${PORT}"
