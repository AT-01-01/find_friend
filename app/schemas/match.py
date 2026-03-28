from pydantic import BaseModel, ConfigDict, Field


class MatchQuery(BaseModel):
    city: str | None = Field(None, description="按城市筛选，可选。")
    interest_keyword: str | None = Field(None, description="按兴趣关键字模糊匹配，可选。")


class MatchUser(BaseModel):
    id: int = Field(..., description="用户 ID。")
    username: str = Field(..., description="用户名。")
    city: str | None = Field(None, description="所在城市。")
    interests: str | None = Field(None, description="兴趣爱好。")

    model_config = ConfigDict(from_attributes=True)
