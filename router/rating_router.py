from typing import List, Optional
from fastapi import APIRouter, File, Form, UploadFile
from schemas.rating_schema import RatingCreate
from services.rating_services import RatingServices
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from oauth2 import get_user_info

router = APIRouter(prefix='/rating',tags=['Rating'])

@router.get('/{rating_id}')
async def get_rating_by_product_id(product_id,db:Session = Depends(get_db)):
    return RatingServices.get_rating_by_product_id(product_id,db)

@router.post('/create')
async def create_rating(
    product_id: int = Form(...),
    details: str = Form(0.0),
    score: int = Form(...),
    files: Optional[List[UploadFile]] = File(None),
    user_data = Depends(get_user_info),
    db:Session = Depends(get_db)):
    return RatingServices.create_rating(product_id,details,score,files,user_data,db)

@router.put('/update')
async def update_rating(
    product_id: int = Form(...),
    details: str = Form(0.0),
    score: int = Form(...),
    files: List[UploadFile] = File(...),
    user_data = Depends(get_user_info),
    db:Session = Depends(get_db)):
    return RatingServices.update_rating(product_id,details,score,files,user_data,db)


@router.delete('/delete')
async def delete_rating(rating_id,
    user_data = Depends(get_user_info),
    db:Session = Depends(get_db)):
    return RatingServices.delete_rating(rating_id,user_data,db)