from fastapi import HTTPException
from starlette import status
from db_queries.order_queries import order_queries
from db_queries.product_queries import product_queries
from db_queries.order_items_queries import order_item_queries
from models.order_model import Order
from models.order_item import OrderItem
from schemas.order_schema import OrderCreate

class OrderServices:
    def get_order_by_id(order_id,user_data,db):
        order_details = order_queries.get_order_by_id(order_id,db)
        if order_details.user_id != user_data['user_id']:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User doesn't have this order!s")
        order_items_details = order_item_queries.get_order_item_by_order_id(order_details.id,db)
        return order_details,order_items_details
    def create_order(order:OrderCreate,user_data,db):
        total_amount = 0
        new_order = Order(
            user_id=user_data["id"],
            order_date=order.order_date,
            payment_method=order.payment_method,
            total_amount=0,
            user_address=order.user_address,
            city=order.city,
            delivery_status=order.delivery_status,
            shipping_cost=order.shipping_cost
        )
        order_queries.add_order(new_order,db)
        order_queries.flush(db)

        for item in order.order_items:
            product = product_queries.get_product_by_id(item.product_id,db)
            if not product:
                raise HTTPException(status_code=404, detail=f"Product with ID {item.product_id} not found")
            
            if product.quantity<item.quantity:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"item with id {item.product_id} have {product.quantity} products left rather than {item.quantity}"
                    )
            
            product.quantity -=item.quantity

            discounted_price = product.price *(product.discount/100)
            total_amount += (product.price - discounted_price) * item.quantity
            
            order_item = OrderItem(
                order_id=new_order.id,
                product_id=item.product_id,
                quantity=item.quantity
            )
            order_item_queries.add_order_item(order_item,db)
        
        new_order.total_amount = total_amount + order.shipping_cost
        order_queries.commit(db)
        
        order_queries.refresh(new_order,db)

        return new_order
    
    def delete_order(order_id,user_data,db):
        order_details = order_queries.get_order_by_id(order_id,db)
        if order_details is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Order doesn't exists")
        if order_details.user_id != user_data['user_id']:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="this order doesnt  belong to this user")

        if order_details.delivery_status is "delivered":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Order has already been delivered!")
        order_queries.delete_order(order_details,db)

        return {"Details":"Order has been deleted successfully!"}