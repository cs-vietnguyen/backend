from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    full_name: str = ""
    phone_number: str = ""


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str
    is_active: bool

    class Config:
        orm_mode = True
