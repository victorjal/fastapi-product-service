from pydantic import BaseModel
from datetime import datetime
from typing import Optional



class ConfigAttribute(BaseModel):
    config_name: str
    config_value: str

class VariantBase(BaseModel):
    id: int
    product_id: int
    sku: str
    sales_price: int
    purchase_price: int
    type: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    config_attributes: list[ConfigAttribute] = []

class VariantCreate(VariantBase):
    pass

class Variant(VariantBase):
    pass 

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    id: int
    name: str
    uom: str
    category_name: str
    is_producible: bool
    is_purchasable: bool
    type: str
    additional_info: Optional[str]
    purchase_uom: Optional[str]
    purchase_uom_conversion_rate: Optional[int]
    batch_tracked: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    variants: list[Variant] = []

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    pass

    class Config:
        orm_mode = True