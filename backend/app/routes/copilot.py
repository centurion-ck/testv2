from fastapi import APIRouter

router = APIRouter(
    prefix="/api"
)

@router.post("/copilot")
def copilot(data: dict):

    prediction = data.get(
        "prediction"
    )

    process_name = data.get(
        "process_name"
    )

    if prediction == "malicious":

        return {

            "incident_id":
            "INC-2026-001",

            "risk_score":
            95,

            "summary":
            f"Threat detected in process {process_name}",

            "root_cause":
            "Cryptomining activity detected",

            "impact":
            "Resource hijacking and workload degradation",

            "actions":[

                "Isolate Pod",

                "Restart Deployment",

                "Scan Container Image",

                "Review RBAC",

                "Notify Security Team"

            ],

            "executive_summary":
            "Critical security incident requires immediate action."

        }

    return {

        "incident_id":
        "INC-2026-002",

        "risk_score":
        10,

        "summary":
        "No active threat detected",

        "root_cause":
        "Normal workload",

        "impact":
        "None",

        "actions":[
            "Continue Monitoring"
        ],

        "executive_summary":
        "Cluster healthy."
    }