from fastapi import APIRouter
from schemas.admin_schema import AdminCreate
from services.admin_services import AdminServices
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from oauth2 import get_user_info

router = APIRouter(prefix='/admin',tags=['Admin'])

@router.get('/{admin_id}')
async def get_admin_by_id(user_details=Depends(get_user_info),db:Session = Depends(get_db)):
    return AdminServices.get_admin_by_id(user_details,db)

@router.post('/create')
async def create_admin(admin:AdminCreate,db:Session = Depends(get_db)):
    return AdminServices.create_admin(admin,db)

@router.put('/update')
async def update_admin(admin:AdminCreate,user_details=Depends(get_user_info),db:Session = Depends(get_db)):
    return AdminServices.update_admin(admin,user_details,db)

@router.delete('/delete')
async def create_admin(admin_id,user_details=Depends(get_user_info),db:Session = Depends(get_db)):
    return AdminServices.delete_admin(admin_id,user_details,db)