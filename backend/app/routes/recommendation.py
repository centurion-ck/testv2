from fastapi import APIRouter

router = APIRouter(
    prefix="/api"
)

@router.post("/recommendation")
def recommendation(data: dict):

    process_name = data.get(
        "process_name",
        ""
    ).lower()

    cpu_usage = data.get(
        "cpu_usage",
        0
    )

    memory_usage = data.get(
        "memory_usage",
        0
    )

    prediction = data.get(
        "prediction",
        "normal"
    )

    severity = "Low"

    actions = []

    root_cause = ""

    impact = ""

    score = 100

    # Crypto Miner

    if process_name in [
        "xmrig",
        "miner",
        "cryptominer"
    ]:

        severity = "Critical"

        score = 20

        root_cause = (
            "Crypto mining activity detected."
        )

        impact = (
            "High CPU consumption may impact cluster workloads."
        )

        actions = [
            "Restart affected pod",
            "Scan container image",
            "Check network connections",
            "Quarantine workload",
            "Notify security team"
        ]

    # High CPU

    elif cpu_usage > 80:

        severity = "High"

        score = 50

        root_cause = (
            "Abnormal CPU utilization detected."
        )

        impact = (
            "Node performance degradation possible."
        )

        actions = [
            "Restart workload",
            "Check application logs",
            "Review scaling policies",
            "Investigate CPU spikes"
        ]

    # High Memory

    elif memory_usage > 800:

        severity = "Medium"

        score = 70

        root_cause = (
            "Excessive memory consumption."
        )

        impact = (
            "Potential OOMKill and service instability."
        )

        actions = [
            "Check memory leak",
            "Review heap usage",
            "Scale deployment",
            "Monitor pod restart count"
        ]

    # Malicious Prediction

    elif prediction == "malicious":

        severity = "Critical"

        score = 30

        root_cause = (
            "AI model classified workload as malicious."
        )

        impact = (
            "Potential security threat."
        )

        actions = [
            "Restart pod",
            "Perform security scan",
            "Generate incident",
            "Notify SOC team"
        ]

    else:

        severity = "Low"

        score = 95

        root_cause = (
            "Normal workload behavior."
        )

        impact = (
            "No significant risk."
        )

        actions = [
            "Continue monitoring"
        ]

    return {

        "security_score": score,

        "severity": severity,

        "root_cause": root_cause,

        "impact": impact,

        "actions": actions
    }