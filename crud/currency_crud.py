from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.currency import Currency
from schemas.currency import CurrencyCreate, CurrencyUpdate


def create_currency(db: Session, currency: CurrencyCreate):
    db_currency = Currency(**currency.dict())
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency


def update_currency(db: Session, currency_id: int, curreny: CurrencyUpdate):
    db_currency = get_currency(db, currency_id)
    if db_currency in None:
        raise HTTPException(status_code=404, detail=f'Currency with id: {currency_id} not found')
    db_currency.name = curreny.name
    db_currency.code = curreny.code
    db.commit()
    db.refresh(db_currency)
    return db_currency


def get_currency(db: Session, currency_id: int):
    return db.query(Currency).filter(Currency.id == currency_id).first()


def get_currencies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Currency).offset(skip).limit(limit).all()


def delete_currency(db: Session, currency_id: int):
    db.query(Currency).filter(Currency.id == currency_id).delete()
    db.commit()
