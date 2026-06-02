import os
import pandas as pd
import mlflow
import mlflow.sklearn

os.environ["MLFLOW_ALLOW_FILE_STORE"] = "true"

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

import joblib

# Force Jenkins MLflow location
os.environ["MLFLOW_TRACKING_URI"] = "file:///var/lib/jenkins/mlruns"

mlflow.set_tracking_uri("file:///var/lib/jenkins/mlruns")

print("MLFLOW URI =", mlflow.get_tracking_uri())

# Create experiment if not exists
experiment_name = "KubeGuardian-AI"

try:
    experiment = mlflow.get_experiment_by_name(
        experiment_name
    )

    if experiment is None:

        mlflow.create_experiment(
            experiment_name,
            artifact_location="file:///var/lib/jenkins/mlruns"
        )

except Exception as e:

    print("Experiment Create Error:", e)

mlflow.set_experiment(experiment_name)

# Load Dataset
df = pd.read_csv(
    "dataset/threats.csv"
)

encoder = LabelEncoder()

df["process_name"] = encoder.fit_transform(
    df["process_name"]
)

X = df[
    [
        "process_name",
        "cpu_usage",
        "memory_usage"
    ]
]

y = df["label"]

with mlflow.start_run():

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    predictions = model.predict(X)

    accuracy = accuracy_score(
        y,
        predictions
    )

    mlflow.log_param(
        "n_estimators",
        100
    )

    mlflow.log_metric(
        "accuracy",
        accuracy
    )

    joblib.dump(
        model,
        "model.pkl"
    )

    joblib.dump(
        encoder,
        "encoder.pkl"
    )

    mlflow.log_artifact(
        "model.pkl"
    )

    mlflow.log_artifact(
        "encoder.pkl"
    )

    print(
        "Accuracy:",
        accuracy    
    )

print("Training Completed")