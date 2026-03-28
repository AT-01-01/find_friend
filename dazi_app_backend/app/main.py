from fastapi import FastAPI

from app.api import api_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.models import activity, chat, user  # noqa: F401

app = FastAPI(title=settings.app_name)
app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
def on_startup() -> None:
    if settings.auto_create_tables:
        Base.metadata.create_all(bind=engine)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "env": settings.app_env}
