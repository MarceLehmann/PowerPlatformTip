#!/bin/bash
# PowerPlatformTip Content Processor v2.0
# Wrapper für Python-Script

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 ist nicht installiert!"
    exit 1
fi

python3 "$SCRIPT_DIR/process-tip.py" "$@"
