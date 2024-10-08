from sqlalchemy import Column, Integer, String, ForeignKey,Float
from sqlalchemy.orm import relationship
from database import Base

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    images = Column(String,nullable=True)
    details = Column(String)
    rating_points = Column(Float)

    # Relationships
    user = relationship("User", back_populates="ratings")
