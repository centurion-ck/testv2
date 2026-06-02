from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Threat

#router = APIRouter()

router = APIRouter(
    prefix="/api"
)

@router.get("/reports")
def reports(
    db: Session = Depends(get_db)
):

    total = db.query(Threat).count()

    malicious = db.query(Threat).filter(
        Threat.prediction == "malicious"
    ).count()

    return {
        "total_threats": total,
        "malicious": malicious
    }