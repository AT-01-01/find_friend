from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.activity import ActivityCreate, ActivityRead
from app.services.activity_service import create_activity, list_activities

router = APIRouter()


@router.post(
    "/",
    response_model=ActivityRead,
    status_code=status.HTTP_201_CREATED,
    summary="发布活动",
    description="创建一条新的活动帖子，返回已创建的活动内容。",
)
def create_activity_post(payload: ActivityCreate, db: Session = Depends(get_db)) -> ActivityRead:
    return create_activity(db, payload)


@router.get(
    "/",
    response_model=list[ActivityRead],
    summary="活动列表",
    description="获取活动帖子列表，按发布时间倒序返回。",
)
def list_activity_posts(db: Session = Depends(get_db)) -> list[ActivityRead]:
    return list_activities(db)
