from pydantic import BaseModel


class RefreshResponseSchema(BaseModel):
    access_token: str


class RefreshRequestSchema(BaseModel):
    refresh_token: str


class LoginResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
    user_id: int
    detail: str


class LoginRequestSchema(BaseModel):
    username: str
    password: str

