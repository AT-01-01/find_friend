from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.models.chat import ChatSession
from app.schemas.chat import ChatSessionCreate


def create_chat_session(db: Session, payload: ChatSessionCreate) -> ChatSession:
    session = ChatSession(user_a_id=payload.user_a_id, user_b_id=payload.user_b_id)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def list_chat_sessions_for_user(db: Session, user_id: int) -> list[ChatSession]:
    stmt = select(ChatSession).where(or_(ChatSession.user_a_id == user_id, ChatSession.user_b_id == user_id))
    return list(db.execute(stmt).scalars().all())
