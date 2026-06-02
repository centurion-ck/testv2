from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Threat

router = APIRouter()

@router.get("/threats")
def get_threats(
    db: Session = Depends(get_db)
):

    threats = db.query(Threat).all()

    return threats