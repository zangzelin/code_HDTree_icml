# HDTree ICML Reproducibility Code

This repository is a minimal public release for reproducing the HDTree ICML experiments on two datasets:

- MNIST
- Limb single-cell data

The code keeps the original training/evaluation path used for the reported runs, but removes lab-specific absolute paths from the public configuration.

## Environment

Create a Python environment with CUDA-enabled PyTorch, then install the pinned Python dependencies:

```bash
pip install -r requirements.txt
```

The experiments were run with a single NVIDIA A100/H20-class GPU. Other CUDA GPUs should work if memory is sufficient. If your CUDA setup requires a different PyTorch wheel, install the matching `torch` and `torchvision` wheels first, then install the remaining packages from `requirements.txt`.

## Data

### MNIST

MNIST is downloaded automatically by `torchvision` into:

```text
./data/mnist
```

### Limb

Place the preprocessed Limb numpy files under:

```text
./data/limb/LimbFilter_data_n.npy
./data/limb/LimbFilter_label.npy
```

The expected shapes are:

```text
LimbFilter_data_n.npy  -> (66633, 500), float32
LimbFilter_label.npy   -> (66633,), int32
```

If starting from `LimbFilter.h5ad`, use:

```bash
python preprocess/pre_limb.py --input_path /path/to/raw --output_path ./data/limb
```

The preprocessing script assumes the raw `.h5ad` file contains `adata.X` and a cell-type column `adata.obs["celltype"]`. It selects the top 500 variable genes, keeps the 10 most frequent cell types, normalizes each selected gene, and writes the two `.npy` files above. The raw Limb file is not redistributed in this repository; obtain it from the dataset source used by your study or place an equivalent `LimbFilter.h5ad` at the input path.

## Training

Run a quick environment smoke test:

```bash
scripts/smoke_test.sh
```

Run MNIST:

```bash
scripts/train_mnist.sh
```

Run Limb:

```bash
scripts/train_limb.sh
```

The public Limb config uses the recommended single-GPU setting from our sweep:

```text
K=10, batch_size=1000, exaggeration_lat=0.5, nu_lat=0.3,
ec_ce_weight=0.5, weightrout=0.5
```

Outputs are written to:

```text
wandb/
checkpoints/
save_near_index/
data/
```

The default configs log clustering and tree metrics every 20 epochs after validation.

## Checkpoint Validation

Validate a trained checkpoint:

```bash
scripts/validate_checkpoint.sh mnist /path/to/checkpoint.pth
```

To compute reconstruction and log-likelihood with diffusion sampling, enable generation:

```bash
python main.py validate \
  -c configs/mnist.yaml \
  --model.init_args.ckpt_path=/path/to/checkpoint.pth \
  --model.init_args.training_str=step2_r \
  --model.init_args.gen_data_bool=True
```

In the internal MNIST run, full training produced:

```text
tree/dp_0          0.93262
tree/lp_0          0.97310
tree/cluster_acc_0 0.97310
tree/nmi_0         0.92999
```

The separate reconstruction validation with `gen_data_bool=True` on 7000 MNIST validation samples produced:

```text
tree/reconstruction_loss_0 44.97935
tree/log_likelihood_0     -13.98696
tree/dp_0                  0.93454
tree/lp_0                  0.97380
tree/cluster_acc_0         0.97380
tree/nmi_0                 0.93277
```

For Limb, the public default config corresponds to the sweep run
`K=10, batch_size=1000, exaggeration_lat=0.5, nu_lat=0.3`. It produced:

```text
tree/dp_0          0.41029
tree/lp_0          0.58370
tree/cluster_acc_0 0.52860
tree/nmi_0         0.49042
```

This setting was selected as the public default because it improved the tree metrics (`DP`, `LP`, `NMI`) over the highest-ACC Limb sweep setting. If optimizing only for clustering accuracy, the alternative `batch_size=2000, nu_lat=0.5` reached `tree/cluster_acc_0=0.54190`.

## Repository Layout

```text
main.py      LightningCLI entrypoint
configs/     MNIST and Limb configs
data_model/  Dataset and datamodule code
model/       HDTree model and diffusion modules
call_backs/  Tree, clustering, and reconstruction evaluation
eval/        Embedding evaluation helpers
preprocess/  Limb preprocessing helper
scripts/     Common train, validation, and smoke-test commands
```

## Notes

- W&B is used in offline mode by default in the commands above.
- Checkpoints are plain PyTorch state dicts saved by `EvalCallBack`.
- The Limb dataset in the paper is referred to as `Limb` in the code and configs.
- The default training scripts accept extra LightningCLI arguments after the script name.
