from pydantic import BaseModel, ConfigDict, Field


class ActivityCreate(BaseModel):
    author_id: int = Field(..., description="发布者用户 ID。")
    title: str = Field(..., description="活动标题。")
    content: str = Field(..., description="活动详情内容。")
    city: str | None = Field(None, description="活动所在城市，可选。")


class ActivityRead(BaseModel):
    id: int = Field(..., description="活动 ID。")
    author_id: int = Field(..., description="发布者用户 ID。")
    title: str = Field(..., description="活动标题。")
    content: str = Field(..., description="活动详情内容。")
    city: str | None = Field(None, description="活动所在城市。")

    model_config = ConfigDict(from_attributes=True)
