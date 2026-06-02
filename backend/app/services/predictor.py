import random

def predict_threat(process_name, cpu, memory):

    dangerous = [
        "xmrig",
        "crypto",
        "miner",
        "netcat",
        "nc",
        "bash"
    ]

    if process_name.lower() in dangerous:

        return {
            "prediction": "malicious",
            "score": 0.98
        }

    if cpu > 90:

        return {
            "prediction": "suspicious",
            "score": 0.75
        }

    return {
        "prediction": "normal",
        "score": 0.10
    }