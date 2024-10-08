from fastapi import APIRouter,Depends
from starlette import status
from services.users_login_services import users_login_services
from oauth2 import create_access_token
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.post('/token')
async def login(User_name,Password,db:Session=Depends(get_db)):
    user_details=users_login_services.authenticate_user(User_name,Password,db)

    access_token = create_access_token(data={"user_id":user_details.id,"is_admin":False})

    if user_details:
        return {"access_token":access_token,"token_type":"bearer"}