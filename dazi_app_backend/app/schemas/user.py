from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    city: str | None = None
    interests: str | None = None
    bio: str | None = None


class LoginRequest(BaseModel):
    username: str
    password: str


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    city: str | None = None
    interests: str | None = None
    bio: str | None = None

    model_config = ConfigDict(from_attributes=True)
