from fastapi import FastAPI
from config.database import Base, engine
from category.routes import categories_router
from products.routes import products_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(products_router)
app.include_router(categories_router)
