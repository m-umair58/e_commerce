from fastapi import HTTPException
from starlette import status
from db_queries.rating_queries import rating_queries
from db_queries.product_queries import product_queries
from models.rating_model import Rating
from schemas.rating_schema import RatingCreate,RatingData
import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="djxncp9l2",
    api_key="678164177725184",
    api_secret="VwB4SHC90XyFrKdc63xf8WR9GFs"
)

class RatingServices:
    def get_rating_by_product_id(product_id,db):
        rating_data = rating_queries.get_rating_by_product_id(product_id,db)
        if rating_data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Rating with this id doesn't exists!")
        return rating_data
        
    def create_rating(product_id, details, score, files, user_data, db):
        if user_data['is_admin'] is True:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only Users can update products")
        if score < 1 or score > 5:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Score must be between 1-5")

        product_details = product_queries.get_product_by_id(product_id, db)
        if product_details is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

        image_urls = []

        if files:
            for file in files:
                if file: 
                    upload_result = cloudinary.uploader.upload(file.file)
                    image_urls.append(upload_result.get("secure_url"))

        
        new_rating = Rating(
            product_id=product_id,
            user_id=user_data['user_id'],
            images=image_urls,
            details=details,
            rating_points=score
        )

        rating_queries.add_rating(new_rating, db)

        return {"Details": "New rating has been added"}

    
    def update_rating(product_id,details,score,files,user_data,db):
        if user_data['is_admin'] is True:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only Users can update products")
        rating_details = rating_queries.get_rating_by_id(id,db)

        if rating_details is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Rating with this id doesn't Exists!")
        
        if rating_details.user_id != user_data['user_id']:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="This user has not posted this rating! ")


        image_urls = []
        for file in files:
            upload_result = cloudinary.uploader.upload(file.file)
            image_urls.append(upload_result.get("secure_url"))


        rating_details.product_id=product_id
        rating_details.user_id = user_data['user_id']
        rating_details.details = details
        rating_details.images = image_urls
        rating_details.rating_points = score

        rating_queries.commit(db)

        return {"Details":"Rating details have been updated"}
    
    def delete_rating(rating_id,user_data,db):
        if user_data['is_admin'] is True:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only Users can update products")

        rating_details = rating_queries.get_rating_by_id(rating_id,db)
        if rating_details is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Rating with this id doesn't Exists!")

        if rating_details.user_id != user_data['user_id']:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="This user has not posted this rating! ")

        rating_queries.delete_rating(rating_details,db)

        return {"Details":"Rating has been deleted"}