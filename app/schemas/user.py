from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    username: str = Field(..., description="用户名，建议唯一。")
    email: EmailStr = Field(..., description="用户邮箱地址。")
    password: str = Field(..., description="登录密码（当前版本仅示例用途）。")
    city: str | None = Field(None, description="所在城市，可用于匹配筛选。")
    interests: str | None = Field(None, description="兴趣爱好，支持自由文本。")
    bio: str | None = Field(None, description="个人简介。")


class LoginRequest(BaseModel):
    username: str = Field(..., description="登录用户名。")
    password: str = Field(..., description="登录密码。")


class UserRead(BaseModel):
    id: int = Field(..., description="用户 ID。")
    username: str = Field(..., description="用户名。")
    email: EmailStr = Field(..., description="邮箱地址。")
    city: str | None = Field(None, description="所在城市。")
    interests: str | None = Field(None, description="兴趣爱好。")
    bio: str | None = Field(None, description="个人简介。")

    model_config = ConfigDict(from_attributes=True)
