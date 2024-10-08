from fastapi import APIRouter
from schemas.order_schema import OrderCreate
from services.order_services import OrderServices
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from oauth2 import get_user_info

router = APIRouter(prefix='/order',tags=['Order'])



@router.get('/{order_id}')
async def get_order_by_id(order_id,user_data = Depends(get_user_info),db:Session = Depends(get_db)):
    return OrderServices.get_order_by_id(order_id,user_data,db)

@router.post('/create')
async def create_order(order:OrderCreate,user_data = Depends(get_user_info),db:Session = Depends(get_db)):
    return OrderServices.create_order(order,user_data,db)

@router.delete('/delete')
async def delete_order(order_id:int,user_data = Depends(get_user_info),db:Session = Depends(get_db)):
    return OrderServices.delete_order(order_id,user_data,db)