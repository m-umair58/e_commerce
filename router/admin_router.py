from fastapi import APIRouter
from schemas.admin_schema import AdminCreate
from services.admin_services import AdminServices
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix='/admin',tags=['Admin'])

@router.get('/{admin_id}')
async def get_admin_by_id(admin_id,db:Session = Depends(get_db)):
    return AdminServices.get_admin_by_id(admin_id,db)

@router.post('/create')
async def create_admin(admin:AdminCreate,db:Session = Depends(get_db)):
    return AdminServices.create_admin(admin,db)

@router.put('/update')
async def update_admin(admin:AdminCreate,db:Session = Depends(get_db)):
    return AdminServices.update_admin(admin,db)

@router.delete('/delete')
async def create_admin(admin_id,db:Session = Depends(get_db)):
    return AdminServices.delete_admin(admin_id,db)