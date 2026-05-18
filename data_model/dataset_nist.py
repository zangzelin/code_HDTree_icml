import numpy as np
import torchvision.datasets as datasets
import logging

from data_model.dataset_meta import DigitsDataset


logger = logging.getLogger(__name__)


class MnistDataset(DigitsDataset):
    """MNIST dataset used in the ICML release."""

    def load_data(self, data_path, train=True):
        train_set = datasets.MNIST(
            root=data_path,
            train=True,
            download=True,
            transform=None,
        )
        test_set = datasets.MNIST(
            root=data_path,
            train=False,
            download=True,
            transform=None,
        )
        data = np.concatenate([train_set.data, test_set.data]).astype(np.float32)
        label = np.concatenate([train_set.targets, test_set.targets]).astype(np.int32)
        data = data.reshape(data.shape[0], -1) / 255.0
        logger.info("MNIST data shape: %s", data.shape)
        return data, label
