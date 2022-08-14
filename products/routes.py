from fastapi import APIRouter, Depends, HTTPException

from config.database import SessionLocal
from config.dependecies import get_db
from . import schemas, crud

products_router = APIRouter(
    prefix="/api/v1/products",
    tags=["Products"]
)


@products_router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: SessionLocal = Depends(get_db)):
    return crud.create_product(db, product)


@products_router.get("/", response_model=list[schemas.Product])
def get_products(category: int | None = None, skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    if category is None:
        return crud.get_products(db, skip, limit)
    return crud.get_products_by_category(db, category, skip, limit)


@products_router.put("/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: SessionLocal = Depends(get_db)):
    return crud.update_product(db, product_id, product)


@products_router.get("/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: SessionLocal = Depends(get_db)):
    return crud.get_product(db, product_id)


@products_router.delete("/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: SessionLocal = Depends(get_db)):
    return crud.delete_product(db, product_id)
