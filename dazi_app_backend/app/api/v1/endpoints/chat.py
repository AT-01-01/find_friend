from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.chat import ChatSessionCreate, ChatSessionRead
from app.services.chat_service import create_chat_session, list_chat_sessions_for_user

router = APIRouter()


@router.post("/sessions", response_model=ChatSessionRead, status_code=status.HTTP_201_CREATED)
def create_session(payload: ChatSessionCreate, db: Session = Depends(get_db)) -> ChatSessionRead:
    return create_chat_session(db, payload)


@router.get("/sessions/{user_id}", response_model=list[ChatSessionRead])
def list_sessions(user_id: int, db: Session = Depends(get_db)) -> list[ChatSessionRead]:
    return list_chat_sessions_for_user(db, user_id)
