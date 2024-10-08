from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import cloudinary.uploader
from database import SessionLocal, engine
from models import Product

app = FastAPI()

# Initialize Cloudinary (use your credentials)


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema for the product request body
class ProductCreate(BaseModel):
    name: str
    price: float
    description: str = None
    discount: float = 0.0
    quantity: int

@app.post("/create-product/")
async def create_product(
    file: UploadFile = File(...),
    product_data: ProductCreate = Depends(),
    db: Session = Depends(get_db)
):
    try:
        # Upload the image to Cloudinary
        upload_result = cloudinary.uploader.upload(file.file)
        image_url = upload_result.get("secure_url")

        # Create a new product instance with the image URL and other data
        new_product = Product(
            name=product_data.name,
            price=product_data.price,
            description=product_data.description,
            image_url=image_url,
            discount=product_data.discount,
            quantity=product_data.quantity
        )

        # Add the new product to the database
        db.add(new_product)
        db.commit()
        db.refresh(new_product)  # Refresh to get the new product's ID or other auto-generated fields

        return {
            "id": new_product.id,
            "name": new_product.name,
            "price": new_product.price,
            "description": new_product.description,
            "image_url": new_product.image_url,
            "discount": new_product.discount,
            "quantity": new_product.quantity
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating product: {str(e)}")
