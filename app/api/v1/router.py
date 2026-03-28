from fastapi import APIRouter

from app.api.v1.endpoints import activity, chat, match, user

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["用户"])
api_router.include_router(match.router, prefix="/match", tags=["匹配"])
api_router.include_router(activity.router, prefix="/activities", tags=["活动"])
api_router.include_router(chat.router, prefix="/chats", tags=["聊天"])
