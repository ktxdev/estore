from fastapi import APIRouter, Depends

from database import SessionLocal
from dependecies import get_db
from schemas.currency import CurrencyCreate, CurrencyUpdate, Currency
from crud import currency_crud

router = APIRouter(
    prefix="/api/v1/currencies",
    tags=["Currencies"]
)


@router.post("/", response_model=Currency)
def create_currency(currency: CurrencyCreate, db: SessionLocal = Depends(get_db)):
    return currency_crud.create_currency(db, currency)


@router.get("/", response_model=list[Currency])
def get_currencies(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    return currency_crud.get_currencies(db, skip, limit)


@router.put("/{product_id}", response_model=Currency)
def update_currency(currency_id: int, currency: CurrencyUpdate, db: SessionLocal = Depends(get_db)):
    return currency_crud.update_currency(db, currency_id, currency)


@router.get("/{product_id}", response_model=Currency)
def get_currency(currency_id: int, db: SessionLocal = Depends(get_db)):
    return currency_crud.get_currency(db, currency_id)


@router.delete("/{product_id}", response_model=Currency)
def delete_currency(currency_id: int, db: SessionLocal = Depends(get_db)):
    return currency_crud.delete_currency(db, currency_id)
