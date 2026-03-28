from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.match import MatchQuery, MatchUser
from app.services.match_service import match_users

router = APIRouter()


@router.post("/search", response_model=list[MatchUser])
def search_matches(payload: MatchQuery, db: Session = Depends(get_db)) -> list[MatchUser]:
    return match_users(db, city=payload.city, interest_keyword=payload.interest_keyword)
