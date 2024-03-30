"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.3
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest


def train_model(train_df: pd.DataFrame, contamination_value: float) -> IsolationForest:
    """Fit an `IsolationForest` model.

    Args:
        train_df (pd.DataFrame): The train `pandas.DataFrame`.
        contamination_value (float): The contamination (percentage of outliers).

    Returns:
        IsolationForest: The fitted `IsolationForest` model.
    """
    clf = IsolationForest(
        random_state=42, bootstrap=True, contamination=contamination_value
    )
    clf.fit(train_df)
    return clf


def predict(ml_model, test_df: pd.DataFrame) -> pd.DataFrame:
    """Predicts the anomalies in the test `pandas.DataFrame`.

    Args:
        ml_model (_type_): A trained model.
        test_df (pd.DataFrame): The test `pandas.DataFrame`.

    Returns:
        pd.DataFrame: The predicted anomalies in the test `pandas.DataFrame`.
    """
    preds = ml_model.predict(test_df)
    preds_mod = np.array(list(map(lambda x: 1 * (x == -1), preds)))

    anomaly_scores = ml_model.score_samples(test_df)
    anomaly_scores_mod = np.array([-x for x in anomaly_scores])

    test_df["ANOMALY"] = preds_mod
    test_df["ANOMALY_SCORE"] = anomaly_scores_mod

    return test_df
