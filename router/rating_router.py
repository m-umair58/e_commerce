from typing import List, Optional
from fastapi import APIRouter, File, Form, UploadFile
from schemas.rating_schema import RatingCreate
from services.rating_services import RatingServices
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix='/rating',tags=['Rating'])

@router.get('/{rating_id}')
async def get_rating_by_product_id(product_id,db:Session = Depends(get_db)):
    return RatingServices.get_rating_by_product_id(product_id,db)

@router.post('/create')
async def create_rating(
    product_id: int = Form(...),
    user_id: int = Form(None),
    details: str = Form(0.0),
    score: int = Form(...),
    files: Optional[List[UploadFile]] = File(None),
    db:Session = Depends(get_db)):
    return RatingServices.create_rating(product_id,user_id,details,score,files,db)

@router.put('/update')
async def update_rating(
    product_id: int = Form(...),
    user_id: int = Form(None),
    details: str = Form(0.0),
    score: int = Form(...),
    files: List[UploadFile] = File(...),
    db:Session = Depends(get_db)):
    return RatingServices.update_rating(product_id,user_id,details,score,files,db)


@router.delete('/delete')
async def delete_rating(rating_id,db:Session = Depends(get_db)):
    return RatingServices.delete_rating(rating_id,db)