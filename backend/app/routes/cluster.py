from fastapi import APIRouter
import subprocess

router = APIRouter(
    prefix="/api",
    tags=["Cluster"]
)

@router.get("/pods-json")
def get_pods_json():

    try:

        result = subprocess.run(
            [
                "kubectl",
                "get",
                "pods",
                "-n",
                "kubeguardian",
                "-o",
                "json"
            ],
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:

        return {
            "error": str(e)
        }