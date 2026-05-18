#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: scripts/validate_checkpoint.sh <mnist|limb> <checkpoint-path> [extra LightningCLI args...]" >&2
  exit 2
fi

dataset="$1"
checkpoint="$2"
shift 2

case "$dataset" in
  mnist) config="configs/mnist.yaml" ;;
  limb) config="configs/limb.yaml" ;;
  *)
    echo "Unknown dataset '$dataset'. Expected 'mnist' or 'limb'." >&2
    exit 2
    ;;
esac

cd "$(dirname "$0")/.."
export WANDB_MODE="${WANDB_MODE:-offline}"

python main.py validate -c "$config" \
  --model.init_args.ckpt_path="$checkpoint" \
  --model.init_args.training_str=step2_r \
  "$@"
