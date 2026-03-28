from pydantic import BaseModel, ConfigDict


class ActivityCreate(BaseModel):
    author_id: int
    title: str
    content: str
    city: str | None = None


class ActivityRead(BaseModel):
    id: int
    author_id: int
    title: str
    content: str
    city: str | None = None

    model_config = ConfigDict(from_attributes=True)
