import os

import numpy as np

from data_model.dataset_meta import DigitsDataset


class LimbDataset(DigitsDataset):
    """Limb single-cell dataset used in the ICML release.

    Expected files under ``data_path``:
      - ``LimbFilter_data_n.npy``: normalized expression matrix, shape (N, 500)
      - ``LimbFilter_label.npy``: integer cell-type labels, shape (N,)

    The original research code used an absolute lab filesystem path.  The
    public release keeps the same preprocessed numpy format but makes the
    directory configurable through ``data.init_args.data_path``.
    """

    def load_data(self, data_path, train=True, filter=True):
        data_file = os.path.join(data_path, "LimbFilter_data_n.npy")
        label_file = os.path.join(data_path, "LimbFilter_label.npy")
        if not os.path.exists(data_file) or not os.path.exists(label_file):
            raise FileNotFoundError(
                "Limb requires LimbFilter_data_n.npy and LimbFilter_label.npy "
                f"under data_path={data_path!r}. See README.md for data setup."
            )

        data = np.load(data_file).astype(np.float32)
        label = np.load(label_file).astype(np.int32)
        return data, label

