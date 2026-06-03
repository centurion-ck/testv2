from fastapi import APIRouter

router = APIRouter(
    prefix="/api"
)

@router.post("/recommendation")
def recommendation(data: dict):

    prediction = data.get(
        "prediction",
        "normal"
    )

    if prediction == "malicious":

        return {
            "security_score": 15,
            "severity": "Critical",
            "root_cause":
            "Crypto miner behavior detected. High CPU and memory usage observed.",

            "impact":
            "Potential resource hijacking and workload degradation.",

            "actions": [
                "Isolate affected pod",
                "Restart workload",
                "Scan container image",
                "Review RBAC permissions",
                "Notify Security Team"
            ]
        }

    return {
        "security_score": 92,
        "severity": "Low",
        "root_cause":
        "No malicious indicators detected.",

        "impact":
        "No impact.",

        "actions": [
            "Continue Monitoring",
            "Review Metrics Periodically"
        ]
    }