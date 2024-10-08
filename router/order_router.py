from typing import List
from fastapi import APIRouter,File, Form, UploadFile
from schemas.order_schema import OrderCreate
from services.order_services import OrderServices
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix='/order',tags=['Order'])



@router.get('/{order_id}')
async def get_order_by_id(order_id,db:Session = Depends(get_db)):
    return OrderServices.get_order_by_id(order_id,db)

@router.post('/create')
async def create_order(order:OrderCreate,db:Session = Depends(get_db)):
    return OrderServices.create_order(order,db)

@router.delete('/delete')
async def delete_order(order_id:int,db:Session = Depends(get_db)):
    return OrderServices.delete_order(order_id,db)