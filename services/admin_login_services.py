from db_queries.user_queries import user_queries
from fastapi import HTTPException
from schemas.user_schema import UserOut
from services.user_services import verify_password
from starlette import status

class admin_login_services:
    def authenticate_admin(Admin_name,Password,db):
        admin_details=user_queries.get_userName(Admin_name,db)

        if admin_details is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Name is Incorrect")
        
        if not verify_password(Password,admin_details.user_password):
            raise HTTPException(status_code=404,detail="Password is Incorrect")
        
        admin_show=UserOut(
            id=admin_details.user_id,
            name=admin_details.user_name
        )
        return admin_show