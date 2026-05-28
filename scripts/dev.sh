#!/usr/bin/env bash
# Bundled helper script: one entry point for common dev tasks.
# Usage: scripts/dev.sh [test|lint|format|all]
set -euo pipefail

cmd="${1:-all}"
case "$cmd" in
  test)   pytest ;;
  lint)   ruff check . ;;
  format) ruff format . ;;
  all)    ruff check . && ruff format --check . && pytest ;;
  *)      echo "usage: scripts/dev.sh [test|lint|format|all]"; exit 1 ;;
esac
