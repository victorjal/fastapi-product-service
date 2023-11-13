from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

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

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class VariantBase(BaseModel):
    sku: str
    sales_price: int
    purchase_price: int

class VariantCreate(VariantBase):
    product_id: int
    type: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class VariantUpdate(VariantBase):
    pass

class Variant(VariantBase):
    id: int
    product: Product

    class Config:
        orm_mode = True

class ConfigAttributeBase(BaseModel):
    config_name: str
    config_value: str

class ConfigAttributeCreate(ConfigAttributeBase):
    variant_id: int

class ConfigAttributeUpdate(ConfigAttributeBase):
    pass

class ConfigAttribute(ConfigAttributeBase):
    variant: Variant

    class Config:
        orm_mode = True