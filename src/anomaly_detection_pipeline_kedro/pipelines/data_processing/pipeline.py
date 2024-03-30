"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from anomaly_detection_pipeline_kedro.pipelines.data_processing.nodes import (
    merge_data,
    process_data,
    train_test_split,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=merge_data,
                inputs="raw_daily_data",
                outputs="merged_data",
                name="node_merge_raw_daily_data",
            ),
            node(
                func=process_data,
                inputs=["merged_data", "params:predictor_cols"],
                outputs="processed_data",
                name="node_process_data",
            ),
            node(
                func=train_test_split,
                inputs="processed_data",
                outputs=["train_data", "test_data", "test_labels"],
                name="node_train_test_split",
            ),
        ]
    )
