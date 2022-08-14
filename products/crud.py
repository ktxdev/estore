from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail=f'Product with id: {product_id} not found')
    db_product.name = product.name
    db_product.description = product.description
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_products_by_category(db: Session, category_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Product).where(models.Product.category_id == category_id).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def delete_product(db: Session, product_id: int):
    db.query(models.Product).filter(models.Product.category_id == product_id).delete()
    db.commit()
