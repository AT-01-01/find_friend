from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_a_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    user_b_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
