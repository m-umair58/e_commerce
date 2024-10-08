from pydantic import BaseModel
from datetime import datetime
from typing import List

class OurModelClass(BaseModel):
    class Config:
        from_attributes = True

from typing import List

class OrderItemCreate(OurModelClass):
    product_id: int
    quantity: int

class OrderCreate(OurModelClass):
    user_id: int
    order_items: List[OrderItemCreate]
    order_date: datetime
    payment_method: str
    user_address: str
    city: str
    delivery_status: str
    shipping_cost: float



class OrderData(OurModelClass):
    id:int
    user_id: int
    order_items: List[OrderItemCreate]
    order_date: datetime
    payment_method: str
    total_amount: float
    user_address: str
    city: str
    delivery_status: str
    shipping_cost: float