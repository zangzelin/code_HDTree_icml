#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
export WANDB_MODE="${WANDB_MODE:-offline}"

python main.py fit -c configs/limb.yaml "$@"
