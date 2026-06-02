from fastapi import APIRouter
import subprocess

router = APIRouter(
    prefix="/api",
    tags=["Kubernetes"]
)

@router.get("/pods")
def get_pods():

    try:

        result = subprocess.run(
            ["kubectl", "get", "pods", "-A"],
            capture_output=True,
            text=True
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except Exception as e:

        return {
            "error": str(e)
        }