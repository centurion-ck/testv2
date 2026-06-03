from fastapi import APIRouter

router = APIRouter(
    prefix="/api"
)

@router.post("/recommendation")
def recommendation(data: dict):

    prediction = data.get("prediction", "normal")

    if prediction == "malicious":

        return {
            "security_score": 15,
            "severity": "Critical",
            "root_cause": "Abnormal CPU and memory consumption consistent with crypto-mining behaviour.",
            "impact": "Cluster performance degradation and possible resource hijacking.",
            "actions": [
                "Isolate affected pod",
                "Restart workload",
                "Scan container image",
                "Review RBAC permissions",
                "Notify security team"
            ]
        }

    return {
        "security_score": 92,
        "severity": "Low",
        "root_cause": "No malicious indicators detected.",
        "impact": "No immediate impact.",
        "actions": [
            "Continue monitoring",
            "Review metrics periodically"
        ]
    }