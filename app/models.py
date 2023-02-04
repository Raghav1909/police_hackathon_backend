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

class PoliceDatabase(Base):
    __tablename__ = "police_database"

    id = Column(Integer, primary_key=True, index=True)
    State = Column(String)
    District_Name =Column(String)
    PS_Name=Column(String)
    FIRNo=Column(String)
    FIR_Date=Column(Date)
    Person_No=Column(String)
    Arrest_Date=Column(Date)
    Person_Name=Column(String)
    Father_Name=Column(String)
    Gender=Column(String)
    AgeWhileOpening=Column(Integer)
    Age= Column(Integer)
    Pres_Address1=Column(String)
    Perm_Address1=Column(String)
    PersonStatus=Column(String)
    Name=Column(String)
    Major_Head=Column(String)
    Minor_Head=Column(String)
    Crime_No=Column(String)
    Arr_ID=Column(String)
    Unit_ID=Column(String)
    FIR_ID=Column(String)
    DEDT=Column(String)

class ICGSDatabase(Base):
    __tablename__ = "ICGS_database"

    id = Column(Integer, primary_key=True, index=True)
    State = Column(String)
    District_Name =Column(String)
    PS_Name=Column(String)
    FIRNo=Column(String)
    FIR_Date=Column(Date)
    Person_No=Column(String)
    Arrest_Date=Column(Date)
    Person_Name=Column(String)
    Father_Name=Column(String)
    Gender=Column(String)
    AgeWhileOpening=Column(Integer)
    Age= Column(Integer)
    Pres_Address1=Column(String)
    Perm_Address1=Column(String)
    PersonStatus=Column(String)
    Name=Column(String)
    Major_Head=Column(String)
    Minor_Head=Column(String)
    Crime_No=Column(String)
    Arr_ID=Column(String)
    Unit_ID=Column(String)
    FIR_ID=Column(String)
    DEDT=Column(String)