from pydantic import BaseModel
from datetime import datetime
from typing import Optional



class ConfigAttributeBase(BaseModel):
    config_value: str

class ConfigAttributeCreate(ConfigAttributeBase):
    pass

class ConfigAttribute(ConfigAttributeBase):   
    config_name: str
    # id:  Optional[int]
    variant_id:  Optional[int] 

    class Config:
        orm_mode = True

class VariantBase(BaseModel):
    sku: str
    sales_price: int
    purchase_price: int
    config_attributes: list[ConfigAttribute] = []

class VariantCreate(VariantBase):
    pass

class Variant(VariantBase):
    id: int
    product_id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
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
    id: int

    class Config:
        orm_mode = True