from pydantic import BaseModel


class CurrencyBase(BaseModel):
    name: str
    code: str


class CurrencyCreate(CurrencyBase):
    pass


class CurrencyUpdate(CurrencyBase):
    pass


class Currency(CurrencyBase):
    id: int
    default: bool
    rateToDefault: float

    class Config:
        orm_mode = True
