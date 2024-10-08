from fastapi import FastAPI
from database import engine
from models.user_model import Base as UserBase
from models.cart_model import Base as CartBase
from models.admin_model import Base as AdminBase
from models.order_model import Base as OrderBase
from models.rating_model import Base as RatingBase
from models.products_model import Base as ProductsBase
from router import user_router,admin_router,product_router,rating_router,order_router,user_login_router,admin_login_router

UserBase.metadata.create_all(bind=engine)
CartBase.metadata.create_all(bind=engine)
AdminBase.metadata.create_all(bind=engine)
OrderBase.metadata.create_all(bind=engine)
RatingBase.metadata.create_all(bind=engine)
ProductsBase.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_login_router.router)
app.include_router(admin_login_router.router)
app.include_router(user_router.router)
app.include_router(admin_router.router)
app.include_router(product_router.router)
app.include_router(rating_router.router)
app.include_router(order_router.router)
