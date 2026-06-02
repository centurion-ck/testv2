from fastapi import APIRouter
import subprocess

router = APIRouter(
    prefix="/api",
    tags=["Auto Remediation"]
)

@router.post("/restart-pod")
def restart_pod(data: dict):

    pod_name = data.get("pod_name")
    namespace = data.get("namespace", "default")

    if not pod_name:
        return {
            "status": "failed",
            "message": "pod_name is required"
        }

    try:

        result = subprocess.run(
            [
                "kubectl",
                "delete",
                "pod",
                pod_name,
                "-n",
                namespace
            ],
            capture_output=True,
            text=True
        )

        return {
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e)
        }