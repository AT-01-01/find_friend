from pydantic import BaseModel, ConfigDict


class MatchQuery(BaseModel):
    city: str | None = None
    interest_keyword: str | None = None


class MatchUser(BaseModel):
    id: int
    username: str
    city: str | None = None
    interests: str | None = None

    model_config = ConfigDict(from_attributes=True)
