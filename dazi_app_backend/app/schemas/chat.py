from pydantic import BaseModel, ConfigDict


class ChatSessionCreate(BaseModel):
    user_a_id: int
    user_b_id: int


class ChatSessionRead(BaseModel):
    id: int
    user_a_id: int
    user_b_id: int

    model_config = ConfigDict(from_attributes=True)
