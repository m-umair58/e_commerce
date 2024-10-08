from db_queries.admin_queries import admin_queries
from fastapi import HTTPException
from schemas.user_schema import UserOut
from services.user_services import verify_password
from starlette import status

class admin_login_services:
    def authenticate_admin(Admin_name,Password,db):
        admin_details=admin_queries.get_adminName(Admin_name,db)

        if admin_details is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Name is Incorrect")
        
        if not verify_password(Password,admin_details.password):
            raise HTTPException(status_code=404,detail="Password is Incorrect")
        
        admin_show=UserOut(
            id=admin_details.id,
            name=admin_details.name
        )
        return admin_show