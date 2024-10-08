from fastapi import APIRouter,Depends
from starlette import status
from services.admin_login_services import admin_login_services
from oauth2 import create_access_token
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="/admin")

@router.post('/token')
async def admin_login(admin_name,Password,db:Session=Depends(get_db)):
    admin_details=admin_login_services.authenticate_admin(admin_name,Password,db)

    access_token = create_access_token(data={"user_id":admin_details.id,"is_admin":True})

    if admin_details:
        return {"access_token":access_token,"token_type":"bearer"}