from fastapi import APIRouter, Depends, HTTPException

from database import SessionLocal
from dependecies import get_db
from crud import category_crud
from schemas.category import Category, CategoryCreate, CategoryUpdate

router = APIRouter(
    prefix="/api/v1/categories",
    tags=["Categories"]
)


@router.post("/", response_model=Category)
def create_category(category: CategoryCreate, db: SessionLocal = Depends(get_db)):
    db_category = category_crud.get_category_by_name(db, category.name)
    if db_category:
        raise HTTPException(status_code=400, detail=f'Category with name: {category.name} already exists')
    return category_crud.create_category(db, category)


@router.get("/", response_model=list[Category])
def get_categories(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    return category_crud.get_categories(db, skip, limit)


@router.put("/{category_id}", response_model=Category)
def update_category(category_id: int, category: CategoryUpdate, db: SessionLocal = Depends(get_db)):
    return category_crud.update_category(db, category_id, category)


@router.get("/{category_id}", response_model=Category)
def get_category(category_id: int, db: SessionLocal = Depends(get_db)):
    return get_category(db, category_id)


@router.delete("/{category_id}", response_model=Category)
def delete_category(category_id: int, db: SessionLocal = Depends(get_db)):
    return category_crud.delete_category(db, category_id)
