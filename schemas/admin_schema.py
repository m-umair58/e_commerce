from pydantic import BaseModel,EmailStr


class OurModelClass(BaseModel):
    class Config:
        from_attributes = True

class AdminCreate(OurModelClass):
    name:str
    email:EmailStr
    password:str

class AdminData(OurModelClass):
    id:int
    name:str
    email:EmailStr
    password:str


class AdminOut(OurModelClass):
    id:int
    name:str

class AdminShow(OurModelClass):
    name:str
    email:EmailStr