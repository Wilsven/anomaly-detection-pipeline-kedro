"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from anomaly_detection_pipeline_kedro.pipelines.data_science.nodes import (
    predict,
    train_model,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=train_model,
                inputs=["train_data", "params:contamination_value"],
                outputs="ml_model",
                name="node_train_model",
            ),
            node(
                func=predict,
                inputs=["ml_model", "test_data"],
                outputs="predictions",
                name="node_predict",
            ),
        ]
    )
