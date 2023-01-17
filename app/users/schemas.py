from pydantic import BaseModel, EmailStr
from datetime import date

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str

    class config:
        orm_mode = True

class UserCreate(UserBase):
    dob: date
    phone_no: str
    is_admin: bool | None = False

