"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

from datetime import datetime as dt
from datetime import timedelta
from typing import Any, Callable

import pandas as pd


def merge_data(partitioned_input: dict[str, Callable[[], Any]]) -> pd.DataFrame:
    """Merge all the raw daily data into a single `pandas.DataFrame`.

    Args:
        partitioned_input (dict[str, Callable[[], Any]]):
            A dictionary containing the `partitions.PartitionedDataset`
            where the values loads the pickle data as `pandas.DataFrame`.

    Returns:
        pd.DataFrame: The merged `pandas.DataFrame`.
    """
    merged_df = pd.DataFrame()
    for _, partition_load_func in sorted(partitioned_input.items()):
        partition_data = partition_load_func()  # Load partition data
        merged_df = pd.concat(
            [merged_df, partition_data], axis=0, ignore_index=True, sort=True
        )
    return merged_df


def process_data(merged_df: pd.DataFrame, predictor_cols: list) -> pd.DataFrame:
    """Process the `pandas.DataFrame`.

    Args:
        merged_df (pd.DataFrame): The merged `pandas.DataFrame`.
        predictor_cols (list): Columns to subset.

    Returns:
        pd.DataFrame: The processed `pandas.DataFrame`.
    """
    merged_df["TX_DATETIME"] = pd.to_datetime(merged_df["TX_DATETIME"])
    merged_df["TX_DATE"] = merged_df["TX_DATETIME"].dt.date
    processed_df = merged_df[predictor_cols]
    return processed_df


def train_test_split(
    processed_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Splits the data into train and test sets.

    Args:
        processed_df (pd.DataFrame): The processed `pandas.DataFrame`.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]: The train, test and test labels.
    """
    processed_df["TX_DATE"] = pd.to_datetime(processed_df["TX_DATE"])
    split_date = processed_df["TX_DATE"].min() + timedelta(days=(8 * 7))
    train_df = processed_df.loc[processed_df["TX_DATE"] <= split_date]
    test_df = processed_df.loc[processed_df["TX_DATE"] > split_date]
    train_df = train_df.drop(columns=["TX_DATE"])
    test_df = test_df.drop(columns=["TX_DATE"])

    # Drop actual label if any (supposed to be unsupervised training)
    if "TX_FRAUD" in train_df.columns:
        train_df = train_df.drop(columns=["TX_FRAUD"])
    if "TX_FRAUD" in test_df.columns:
        test_labels = test_df[["TX_FRAUD"]]  # Store test labels (if any)
        test_df = test_df.drop(columns=["TX_FRAUD"])
    else:
        test_labels = pd.DataFrame()  # Empty dataframe if no test label

    return train_df, test_df, test_labels
