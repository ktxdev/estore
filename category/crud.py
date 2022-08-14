from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category_id: int, category: schemas.CategoryUpdate):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail=f'Category with id: {category_id} not found')
    db_category.name = category.name
    db.commit()
    db.refresh(db_category)
    return db_category


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_category_by_name(db: Session, category_name: str):
    return db.query(models.Category).filter(models.Category.name == category_name).first()


def delete_category(db: Session, category_id: int):
    db.query(models.Category).filter(models.Category.id == category_id).delete()
    db.commit()
