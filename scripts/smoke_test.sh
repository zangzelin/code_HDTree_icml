#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
export WANDB_MODE="${WANDB_MODE:-offline}"

python main.py fit -c configs/mnist.yaml \
  --trainer.max_epochs=1 \
  --trainer.limit_train_batches=1 \
  --trainer.limit_val_batches=1 \
  --trainer.num_sanity_val_steps=0 \
  --trainer.logger=false \
  --trainer.enable_checkpointing=false \
  --trainer.enable_progress_bar=false \
  "$@"
