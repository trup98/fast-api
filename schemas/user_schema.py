from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    user_name: str
    email: EmailStr


class UserCreate(UserBase):
    first_name: str
    last_name: str


class UserUpdate(BaseModel):
    user_name: str
    first_name: str
    last_name: str


class UserOut(BaseModel):
    user_name: str
    email: EmailStr
    first_name: str
    last_name: str

    class Config:
        orm_mode = True
