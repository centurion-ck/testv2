from fastapi import APIRouter
import subprocess

router = APIRouter(
    prefix="/api"
)

@router.get("/cluster-metrics")
def cluster_metrics():

    result = subprocess.run(
        ["kubectl", "top", "pods", "-A"],
        capture_output=True,
        text=True
    )

    return {
        "metrics": result.stdout
    }