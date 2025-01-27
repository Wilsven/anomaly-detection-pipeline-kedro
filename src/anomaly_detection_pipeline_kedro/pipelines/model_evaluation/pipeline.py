"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from anomaly_detection_pipeline_kedro.pipelines.model_evaluation.nodes import (
    evaluate_model,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=evaluate_model,
                inputs=["predictions", "test_labels"],
                outputs="evaluation_plot",
                name="node_model_evaluation",
            )
        ]
    )
