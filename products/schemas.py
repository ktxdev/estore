from pydantic import BaseModel
from category.schemas import Category


class ProductBase(BaseModel):
    name: str
    description: str


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    category: Category

    class Config:
        orm_mode = True

# class User(UserBase):
#     id: int
#     is_active: bool
#     items: list[Item] = []
#
#     class Config:
#         orm_mode = True
