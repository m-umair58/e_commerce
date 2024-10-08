from schemas.admin_schema import AdminCreate,AdminShow,AdminData
from db_queries.admin_queries import admin_queries
from fastapi import HTTPException
from starlette import status
from models.admin_model import Admin
from passlib.context import CryptContext

bcrypt_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
def get_password_hash(password):
    return bcrypt_context.hash(password)

def verify_password(plain_password,hashed_password):
    return bcrypt_context.verify(plain_password,hashed_password)

class AdminServices:
    def get_admin_by_id(admin_id,db):
        return admin_queries.get_admin_by_id(admin_id,db)
    
    def create_admin(admin:AdminCreate,db):
        admin_data= admin_queries.get_admin_by_email(admin.email,db)
        if admin_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Admin with this email already exists!")

        new_admin = Admin(
            name = admin.name,
            email =  admin.email,
            password =get_password_hash(admin.password),
        )

        admin_queries.add_admin(new_admin,db)
        return_admin=AdminShow(
            name=admin.name,
            email=admin.email
        )
        return return_admin
    
    def update_admin(admin:AdminData,db):
        admin_data= admin_queries.get_admin_by_email(admin.email,db)
        if not admin_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Admin with this email doesn't exists!")
        
        admin_data.name = admin.name,
        admin_data.email =  admin.email,
        admin_data.password = get_password_hash(admin.password)

        admin_queries.commit(db)

        return {"Details":"Admin has been updated"}
    
    def delete_admin(admin_id,db):
        admin_data= admin_queries.get_admin_by_id(admin_id,db)
        if not admin_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Admin with this email doesn't exists!")
        
        admin_queries.delete_admin(admin_data,db)

        return {"Message":"Admin has been deleted successfully"}