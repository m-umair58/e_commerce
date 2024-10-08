from fastapi import HTTPException
from starlette import status
from db_queries.product_queries import product_queries
from models.products_model import Product
import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="djxncp9l2",
    api_key="678164177725184",
    api_secret="VwB4SHC90XyFrKdc63xf8WR9GFs"
)

class ProductServices:
    def get_product_by_id(product_id,db):
        product_data = product_queries.get_product_by_id(product_id,db)
        if product_data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Product with this id doesn't exists!")
        return product_data
        
    def create_product(name,price,description,discount,quantity,files,user_data,db):
        if user_data['is_admin'] is False:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only admins can add products")
        image_urls = []
        for file in files:
            upload_result = cloudinary.uploader.upload(file.file)
            image_urls.append(upload_result.get("secure_url"))

        if price<=0:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Price of Product should be greater than 0")
        
        if discount <0 or discount>99:            
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Discount shloud be between 0-99%")
        
        if quantity<1:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Product quantity should be greater than 1")

        new_product = Product(
            name = name,
            price = price,
            description = description,
            images = image_urls,
            discount = discount,
            quantity = quantity
        )

        product_queries.add_product(new_product,db)
        return new_product
    
    def update_product(product_id,name,price,description,discount,quantity,files,user_data,db):
        if user_data['is_admin'] is False:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only admins can update products")
        product_details = product_queries.get_product_by_id(product_id,db)

        if product_details is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product with this id doesn't Exists!")
        
        image_urls = []
        for file in files:
            upload_result = cloudinary.uploader.upload(file.file)
            image_urls.append(upload_result.get("secure_url"))

        product_details.name=name
        product_details.price=price
        product_details.description=description
        product_details.images = image_urls
        product_details.discount = discount
        product_details.quantity = quantity

        product_queries.commit(db)

        return {"Details":"Product details have been updated"}
    
    def delete_product(product_id,user_data,db):
        if user_data['is_admin'] is False:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Only admins can delete products")
        product_details = product_queries.get_product_by_id(product_id,db)
        if product_details is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product with this id doesn't Exists!")

        product_queries.delete_product(product_details,db)

        return {"Details":"Product has been deleted"}