from models.order_model import Order
from sqlalchemy.orm import Session

class order_queries:
    def get_order_by_id(order_id,db:Session):
        return db.query(Order).filter(Order.id==order_id).first()

    def add_order(order,db:Session):
        db.add(order)
        db.commit()
        db.refresh(order)

    def commit(db:Session):
        db.commit()

    def delete_order(order,db:Session):
        db.delete(order)
        db.commit()