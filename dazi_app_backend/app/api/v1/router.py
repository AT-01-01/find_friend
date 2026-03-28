from fastapi import APIRouter

from app.api.v1.endpoints import activity, chat, match, user

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(match.router, prefix="/match", tags=["match"])
api_router.include_router(activity.router, prefix="/activities", tags=["activities"])
api_router.include_router(chat.router, prefix="/chats", tags=["chats"])
