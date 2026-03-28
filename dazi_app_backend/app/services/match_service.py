from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def match_users(db: Session, city: str | None = None, interest_keyword: str | None = None) -> list[User]:
    stmt = select(User)
    if city:
        stmt = stmt.where(User.city == city)
    if interest_keyword:
        stmt = stmt.where(User.interests.ilike(f"%{interest_keyword}%"))
    return list(db.execute(stmt).scalars().all())
