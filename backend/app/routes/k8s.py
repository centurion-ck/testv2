from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.get("/pods")
def get_pods():

    try:

        result = subprocess.check_output(
            [
                "kubectl",
                "get",
                "pods",
                "-A",
                "-o",
                "json"
            ]
        )

        return result.decode()

    except Exception as e:

        return {
            "error": str(e)
        }