from models.order_item import OrderItem
from sqlalchemy.orm import Session

class order_item_queries:
    def get_order_item_by_order_id(order_id,db:Session):
        return db.query(OrderItem).filter(OrderItem.order_id==order_id).all()

    def add_order_item(order_item,db:Session):
        db.add(order_item)
        db.commit()
        db.refresh(order_item)

    def commit(db:Session):
        db.commit()

    def delete_order_item(order_item,db:Session):
        db.delete(order_item)
        db.commit()