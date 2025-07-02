from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    user_name: str
    email: EmailStr
    first_name: str
    last_name: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
