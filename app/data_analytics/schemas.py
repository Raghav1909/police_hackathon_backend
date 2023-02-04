from pydantic import BaseModel

class PoliceDatabaseInDB(BaseModel):
    State : str
    District_Name :str
    PS_Name:str
    FIRNo:str
    FIR_Date:str
    Person_No:str
    Arrest_Date:str
    Person_Name:str
    Father_Name:str
    Gender:str
    AgeWhileOpening:str
    Age: str
    Pres_Address1:str
    Perm_Address1:str
    PersonStatus:str
    Name:str
    Major_Head:str
    Minor_Head:str
    Crime_No:str
    Arr_ID:str
    Unit_ID:str
    FIR_ID:str
    DEDT:str

class Filter(BaseModel):
    state: list = []
    district: list = []
    ps_name: str
    gender: list = []
    age: list = []