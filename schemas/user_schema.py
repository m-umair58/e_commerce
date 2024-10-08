from pydantic import BaseModel,EmailStr


class OurModelClass(BaseModel):
    class Config:
        from_attributes = True

class UserCreate(OurModelClass):
    name:str
    email:EmailStr
    password:str
    phone_number:str

class UserData(OurModelClass):
    id:int
    name:str
    email:EmailStr
    password:str
    phone_number:str


class UserOut(OurModelClass):
    id:int
    name:str

class UserShow(OurModelClass):
    name:str
    email:EmailStr