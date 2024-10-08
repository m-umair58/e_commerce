from models.products_model import Product
from sqlalchemy.orm import Session

class product_queries:
    def get_product_by_id(product_id,db:Session):
        return db.query(Product).filter(Product.id==product_id).first()
    
    def get_productName(product_name,db:Session):
        return db.query(Product).filter(Product.name==product_name).first()

    def add_product(product,db:Session):
        db.add(product)
        db.commit()
        db.refresh(product)

    def commit(db:Session):
        db.commit()

    def delete_product(product,db:Session):
        db.delete(product)
        db.commit()