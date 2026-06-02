import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

import joblib

mlflow.set_experiment("KubeGuardian-AI")

df = pd.read_csv("dataset/threats.csv")

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

    mlflow.sklearn.log_model(
        model,
        "model"
    )

    joblib.dump(
        model,
        "model.pkl"
    )

    joblib.dump(
        encoder,
        "encoder.pkl"
    )

    print(
        "Accuracy:",
        accuracy
    )
