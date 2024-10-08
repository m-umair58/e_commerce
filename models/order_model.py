from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    order_date = Column(DateTime)
    payment_method = Column(String)
    total_amount = Column(Float)
    user_address = Column(String)
    city = Column(String)
    shipping_cost = Column(Float)
    delivery_status = Column(String)

    user = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")
