from schemas.user_schema import UserCreate,UserShow,UserData
from db_queries.user_queries import user_queries
from fastapi import HTTPException
from starlette import status
from models.user_model import User
from passlib.context import CryptContext

bcrypt_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
def get_password_hash(password):
    return bcrypt_context.hash(password)

def verify_password(plain_password,hashed_password):
    return bcrypt_context.verify(plain_password,hashed_password)

class UserServices:
    def get_user_by_id(user_data,db):
        if user_data['is_admin'] is True:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only user can access this")
        user_data = user_queries.get_user_by_id(user_data['id'],db)
        if user_data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with this id doesn't exists!")
    
    def create_user(user:UserCreate,db):
        user_data= user_queries.get_user_by_email(user.email,db)
        if user_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with this email already exists!")
        
        if len(user.phone_number)!=11:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Phone Number should be of length 11!")

        new_user = User(
            name = user.name,
            email =  user.email,
            password =get_password_hash(user.password),
            phone_number = user.phone_number,
        )

        user_queries.add_user(new_user,db)
        return_user=UserShow(
            name=user.name,
            email=user.email
        )
        return return_user
    
    def update_user(user:UserCreate,user_data,db):
        if user_data['is_admin'] is True:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only user can access this")
        user_data= user_queries.get_user_by_email(user.email,db)# shlould be changes using id
        if not user_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with this email doesn't exists!")
        
        user_data.name = user.name,
        user_data.email =  user.email,
        user_data.password =get_password_hash(user.password),
        user_data.phone_number = user.phone_number


        user_queries.commit(db)

        return {"Details":"User data has been updated"}
    
    def delete_user(user_id,user_details,db):
        if user_details['is_admin'] is True:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only user can access this")
        user_data= user_queries.get_user_by_id(user_id,db)
        if not user_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with this id doesn't exists!")
        
        user_queries.delete_user(user_data,db)

        return {"Message":"User has been deleted successfully"}