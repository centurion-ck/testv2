from fastapi import APIRouter

router = APIRouter()

@router.post("/predict")
def predict(data: dict):

    process_name = data.get("process_name")

    if process_name.lower() == "xmrig":
        return {
            "prediction": "malicious",
            "score": 0.98
        }

    return {
        "prediction": "normal",
        "score": 0.10
    }