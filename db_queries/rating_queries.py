from models.rating_model import Rating
from sqlalchemy.orm import Session

class rating_queries:
    def get_rating_by_id(rating_id,db:Session):
        return db.query(Rating).filter(Rating.id==rating_id).first()

    def get_rating_by_product_id(product_id,db:Session):
        return db.query(Rating).filter(Rating.product_id==product_id).all()

    def add_rating(rating,db:Session):
        db.add(rating)
        db.commit()
        db.refresh(rating)

    def commit(db:Session):
        db.commit()

    def delete_rating(rating,db:Session):
        db.delete(rating)
        db.commit()