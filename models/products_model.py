from sqlalchemy import Column, Integer, String, Float,ARRAY
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String)
    images = Column(String)  # Could be a list of image URLs
    discount = Column(Float)
    quantity = Column(Integer)

