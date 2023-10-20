from pydantic import BaseModel


class User(BaseModel):
    id: int | None
    username: str
    hashed_password: str
    salt: str

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True
