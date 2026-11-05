import mlflow
import pandas as pd

mlflow.set_experiment(
    "eduassist_llmops_assignment"
)

df = pd.read_csv(
    "data/outputs/prompt_evaluation_results.csv"
)

for _, row in df.iterrows():

    with mlflow.start_run(
        run_name=row["prompt_version"]
    ):

        mlflow.log_param(
            "prompt_version",
            row["prompt_version"]
        )

        mlflow.log_metric(
            "avg_latency_seconds",
            row["avg_latency_seconds"]
        )

        mlflow.log_metric(
            "avg_input_tokens",
            row["avg_input_tokens"]
        )

        mlflow.log_metric(
            "avg_output_tokens",
            row["avg_output_tokens"]
        )

        mlflow.log_metric(
            "avg_cost_per_request",
            row["avg_cost_per_request"]
        )

        if pd.notna(row["valid_json"]):
            mlflow.log_metric(
                "valid_json",
                row["valid_json"]
            )

print("MLflow logging completed.")