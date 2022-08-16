from fastapi import APIRouter
from api.v1 import category, currency, file, product

routes = APIRouter()

routes.include_router(file.router)
routes.include_router(product.router)
routes.include_router(category.router)
routes.include_router(currency.router)
