from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    total_cost = Column(Float, nullable=False)
    shipping_cost = Column(Float, nullable=False)

    # Relationships
    user = relationship("User", back_populates="cart")
    product = relationship("Product")
