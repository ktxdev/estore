from fastapi import APIRouter
from api.v1 import category, currency, file, product

router = APIRouter()

router.include_router(file.router)
router.include_router(product.router)
router.include_router(category.router)
router.include_router(currency.router)
