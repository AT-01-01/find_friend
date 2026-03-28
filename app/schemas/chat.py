from pydantic import BaseModel, ConfigDict, Field


class ChatSessionCreate(BaseModel):
    user_a_id: int = Field(..., description="会话参与者 A 的用户 ID。")
    user_b_id: int = Field(..., description="会话参与者 B 的用户 ID。")


class ChatSessionRead(BaseModel):
    id: int = Field(..., description="聊天会话 ID。")
    user_a_id: int = Field(..., description="参与者 A 的用户 ID。")
    user_b_id: int = Field(..., description="参与者 B 的用户 ID。")

    model_config = ConfigDict(from_attributes=True)
