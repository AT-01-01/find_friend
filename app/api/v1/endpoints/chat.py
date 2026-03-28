from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.chat import ChatSessionCreate, ChatSessionRead
from app.services.chat_service import create_chat_session, list_chat_sessions_for_user

router = APIRouter()


@router.post(
    "/sessions",
    response_model=ChatSessionRead,
    status_code=status.HTTP_201_CREATED,
    summary="创建聊天会话",
    description="根据两位用户 ID 创建一条聊天会话关系。",
)
def create_session(payload: ChatSessionCreate, db: Session = Depends(get_db)) -> ChatSessionRead:
    return create_chat_session(db, payload)


@router.get(
    "/sessions/{user_id}",
    response_model=list[ChatSessionRead],
    summary="查询用户聊天会话",
    description="根据用户 ID 查询该用户参与的全部聊天会话。",
)
def list_sessions(user_id: int, db: Session = Depends(get_db)) -> list[ChatSessionRead]:
    return list_chat_sessions_for_user(db, user_id)
