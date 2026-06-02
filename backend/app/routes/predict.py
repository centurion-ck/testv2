from fastapi import APIRouter
import joblib
import json
from datetime import datetime

router = APIRouter()

model = joblib.load("/app/model.pkl")
encoder = joblib.load("/app/encoder.pkl")


@router.post("/predict")
def predict(data: dict):

    process_name = data.get("process_name")
    cpu_usage = data.get("cpu_usage")
    memory_usage = data.get("memory_usage")

    try:
        process_encoded = encoder.transform(
            [process_name]
        )[0]
    except:
        process_encoded = 0

    prediction = model.predict(
        [[
            process_encoded,
            cpu_usage,
            memory_usage
        ]]
    )[0]

    probability = model.predict_proba(
        [[
            process_encoded,
            cpu_usage,
            memory_usage
        ]]
    )[0]

    score = round(max(probability), 2)

    if prediction == 1:

        result = {
            "prediction": "malicious",
            "score": score,
            "severity": "Critical",
            "recommendation": "Terminate Container",
            "threat_type": "Crypto Miner"
        }

    else:

        result = {
            "prediction": "normal",
            "score": score,
            "severity": "Low",
            "recommendation": "Monitor",
            "threat_type": "None"
        }

    event = {
        "timestamp": str(datetime.now()),
        "process_name": process_name,
        "prediction": result["prediction"],
        "severity": result["severity"]
    }

    try:
        with open("/app/threat_log.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(event)

    with open("/app/threat_log.json", "w") as f:
        json.dump(logs, f, indent=4)

    return result


@router.get("/history")
def history():

    try:
        with open("/app/threat_log.json", "r") as f:
            return json.load(f)
    except:
        return []


@router.get("/stats")
def stats():

    try:
        with open("/app/threat_log.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []

    total = len(logs)

    critical = len(
        [
            x for x in logs
            if x["severity"] == "Critical"
        ]
    )

    low = len(
        [
            x for x in logs
            if x["severity"] == "Low"
        ]
    )

    return {
        "total": total,
        "critical": critical,
        "low": low
    }
