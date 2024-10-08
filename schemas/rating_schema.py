from pydantic import BaseModel

class OurModelClass(BaseModel):
    class Config:
        from_attributes = True

class RatingCreate(OurModelClass):
    product_id:int
    user_id:int
    images:str
    details:str
    score:int

class RatingData(OurModelClass):
    id:int
    product_id:int
    user_id:int
    images:str
    details:str
    score:int
