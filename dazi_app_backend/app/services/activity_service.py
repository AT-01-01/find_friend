from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.activity import ActivityPost
from app.schemas.activity import ActivityCreate


def create_activity(db: Session, payload: ActivityCreate) -> ActivityPost:
    post = ActivityPost(
        author_id=payload.author_id,
        title=payload.title,
        content=payload.content,
        city=payload.city,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def list_activities(db: Session) -> list[ActivityPost]:
    stmt = select(ActivityPost).order_by(ActivityPost.id.desc())
    return list(db.execute(stmt).scalars().all())
