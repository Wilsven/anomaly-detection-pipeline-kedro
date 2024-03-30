from pathlib import PurePosixPath
from typing import Any

import fsspec
import numpy as np
import pandas as pd
from kedro.io import AbstractDataset
from kedro.io.core import get_filepath_str, get_protocol_and_path


class PandasPickleDataset(AbstractDataset[np.ndarray, np.ndarray]):
    """``PandasPickleDataset`` loads / save pickle data from a given filepath as `pandas.DataFrame` using pandas.

    Example:
    ::

        >>> PandasPickleDataset(filepath='/img/file/path.pkl')
    """

    def __init__(self, filepath: str):
        """Creates a new instance of PandasPickleDataset to load / save pickle data for given filepath.

        Args:
            filepath (str): The location of the pickle file to load / save data.
        """
        protocol, path = get_protocol_and_path(filepath)
        self._protocol = protocol
        self._filepath = PurePosixPath(path)
        self._fs = fsspec.filesystem(self._protocol)

    def _load(self) -> pd.DataFrame:
        """Loads data from the pickle file.

        Returns:
            pd.DataFrame: Data from the pickle file as a `pandas.DataFrame`.
        """
        # using get_filepath_str ensures that the protocol and path are appended correctly for different filesystems
        load_path = get_filepath_str(self._filepath, self._protocol)
        with self._fs.open(load_path) as f:
            df = pd.read_pickle(f)
            return df

    def _save(self, data: pd.DataFrame) -> None:
        """Saves pickle data to the specified filepath.

        Args:
            data (pd.DataFrame): The saved pickle file.
        """
        save_path = get_filepath_str(self._filepath, self._protocol)
        with self._fs.open(save_path, mode="wb") as f:
            data.to_pickle(f)

    def _describe(self) -> dict[str, Any]:
        """Returns a dict that describes the attributes of the dataset."""
        return dict(filepath=self._filepath, protocol=self._protocol)
