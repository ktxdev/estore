from fastapi import APIRouter, Depends

from database import SessionLocal
from dependecies import get_db
from schemas.product import ProductCreate, Product, ProductUpdate
from crud import product_crud

router = APIRouter(
    prefix="/api/v1/products",
    tags=["Products"]
)


@router.post("/", response_model=Product)
def create_product(product: ProductCreate, db: SessionLocal = Depends(get_db)):
    return product_crud.create_product(db, product)


@router.get("/", response_model=list[Product])
def get_products(category: int | None = None, skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    if category is None:
        return product_crud.get_products(db, skip, limit)
    return product_crud.get_products_by_category(db, category, skip, limit)


@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate, db: SessionLocal = Depends(get_db)):
    return product_crud.update_product(db, product_id, product)


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, db: SessionLocal = Depends(get_db)):
    return product_crud.get_product(db, product_id)


@router.delete("/{product_id}", response_model=Product)
def delete_product(product_id: int, db: SessionLocal = Depends(get_db)):
    return product_crud.delete_product(db, product_id)
