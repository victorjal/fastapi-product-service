from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Config_Attributes(BaseModel):
    config_name: str
    config_value: str

class Variant(BaseModel):
    id: int
    sku: str
    sales_price: int
    product_id: int
    purchase_price: int
    type: str
    created_at: str
    updated_at: str
    config_attributes: List[Config_Attributes]


class Product(BaseModel):
    id: int
    name: str
    uom: str
    category_name: str
    is_producible: bool
    is_purchasable: bool
    type: str
    purchase_uom: str
    purchase_uom_conversion_rate: int
    batch_tracked: bool
    variants: List[Variant]
    additional_info: str
    created_at: str
    updated_at: str


@app.post("/v1/products/create")
def create_product(product: Product):
    # TODO save database
    return product
