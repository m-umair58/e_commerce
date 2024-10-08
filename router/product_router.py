from typing import List
from fastapi import APIRouter,File, Form, UploadFile
from schemas.product_schema import ProductCreate
from services.product_services import ProductServices
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

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
    db:Session = Depends(get_db)):
    return ProductServices.create_product(name,price,description,discount,quantity,files,db)

@router.put('/update')
async def update_product(
    name: str = Form(...),
    price: float = Form(...),
    description: str = Form(None),
    discount: float = Form(0.0),
    quantity: int = Form(...),
    files: List[UploadFile] = File(...),
    db:Session = Depends(get_db)):
    return ProductServices.update_product(name,price,description,discount,quantity,files,db)

@router.delete('/delete')
async def create_product(product_id,db:Session = Depends(get_db)):
    return ProductServices.delete_product(product_id,db)