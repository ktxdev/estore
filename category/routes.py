from fastapi import APIRouter, Depends, HTTPException

from config.database import SessionLocal
from config.dependecies import get_db
from . import schemas, crud

categories_router = APIRouter(
    prefix="/api/v1/categories",
    tags=["Categories"]
)


@categories_router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: SessionLocal = Depends(get_db)):
    db_category = crud.get_category_by_name(db, category.name)
    if db_category:
        raise HTTPException(status_code=400, detail=f'Category with name: {category.name} already exists')
    return crud.create_category(db, category)


@categories_router.get("/", response_model=list[schemas.Category])
def get_categories(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    return crud.get_categories(db, skip, limit)


@categories_router.put("/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryUpdate, db: SessionLocal = Depends(get_db)):
    return crud.update_category(db, category_id, category)


@categories_router.get("/{category_id}", response_model=schemas.Category)
def get_category(category_id: int, db: SessionLocal = Depends(get_db)):
    return crud.get_category(db, category_id)


@categories_router.delete("/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: SessionLocal = Depends(get_db)):
    return crud.delete_category(db, category_id)
