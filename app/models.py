from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from database import Base

class User(Base):
    __tablename__ = "users"

    username = Column(String, unique=True, index=True, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String) # hashed password
    dob = Column(Date)
    phone_no = Column(String)
    is_admin = Column(Boolean, default=False)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email}, is_active={self.is_active})"