from typing import List
from fastapi import APIRouter,File, Form, UploadFile
from schemas.product_schema import ProductCreate
from services.product_services import ProductServices
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from oauth2 import get_user_info

router = APIRouter(prefix='/product',tags=['Product'])



@router.get('/{product_id}')
async def get_product_by_id(product_id,db:Session = Depends(get_db)):
    return ProductServices.get_product_by_id(product_id,db)

@router.post('/create')
async def create_product(
    name: str = Form(...),
    price: float = Form(...),
    description: str = Form(None),
    discount: float = Form(0.0),
    quantity: int = Form(...),
    files: List[UploadFile] = File(...),
    user_data = Depends(get_user_info),
    db:Session = Depends(get_db)):
    return ProductServices.create_product(name,price,description,discount,quantity,files,user_data,db)

@router.put('/update')
async def update_product(
    product_id: int = Form(...),
    name: str = Form(...),
    price: float = Form(...),
    description: str = Form(None),
    discount: float = Form(0.0),
    quantity: int = Form(...),
    files: List[UploadFile] = File(...),
    user_data = Depends(get_user_info),
    db:Session = Depends(get_db)):
    return ProductServices.update_product(product_id,name,price,description,discount,quantity,files,user_data,db)

@router.delete('/delete')
async def create_product(product_id,
    user_data = Depends(get_user_info),
    db:Session = Depends(get_db)):
    return ProductServices.delete_product(product_id,user_data,db)