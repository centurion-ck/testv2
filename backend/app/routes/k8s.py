from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.get("/pods")
def get_pods():
    try:
        result = subprocess.check_output(
            ["kubectl", "get", "pods", "-A"]
        ).decode()

        return {"pods": result}

    except Exception as e:
        return {"error": str(e)}