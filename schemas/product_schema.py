from pydantic import BaseModel

class OurModelClass(BaseModel):
    class Config:
        from_attributes = True

class ProductCreate(OurModelClass):
    name:str
    price:int
    description:str
    rating_id:int
    discount:int
    quantity:int

class ProductData(OurModelClass):
    id:int
    name:str
    price:int
    description:str
    rating_id:int
    discount:int
    quantity:int
