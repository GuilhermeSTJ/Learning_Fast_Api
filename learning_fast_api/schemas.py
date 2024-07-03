from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class User(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDB(User):
    id: int


class Count(BaseModel):
    in_value1: int
    in_value2: int


class CountSaida(Count):
    out_value: int


class UserList(BaseModel):
    users: list[UserPublic]
