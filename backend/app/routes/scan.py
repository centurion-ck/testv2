from fastapi import APIRouter
import subprocess

router = APIRouter(
    prefix="/api",
    tags=["Scanner"]
)

@router.get("/scan-cluster")
def scan_cluster():

    try:

        result = subprocess.check_output(
            [
                "kubectl",
                "top",
                "pods",
                "-A"
            ]
        ).decode()

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e)
        }