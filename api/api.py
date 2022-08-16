from fastapi import APIRouter
from api.v1 import category, product

routes = APIRouter()

routes.include_router(category.router)
routes.include_router(product.router)