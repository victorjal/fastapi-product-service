from fastapi import Depends, FastAPI, HTTPException
from . import crud, models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session


# from typing import Union, List
# from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# class Config_Attributes(BaseModel):
#    config_name: str
#    config_value: str

# class Variant(BaseModel):
#    id: int
#    sku: str
#    sales_price: int
#    product_id: int
#    purchase_price: int
#    type: str
#    created_at: str
#    updated_at: str
#    config_attributes: List[Config_Attributes]


# class Product(BaseModel):
#    id: int
#    name: str
#    uom: str
#    category_name: str
#    is_producible: bool
#    is_purchasable: bool
#    type: str
#    purchase_uom: str
#    purchase_uom_conversion_rate: int
#    batch_tracked: bool
#    variants: List[Variant]
#    additional_info: str
#    created_at: str
#    updated_at: str


@app.post("/v1/products/create", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    # TODO save database
    db_product = crud.create_product(db, product)
    if db_product:
        raise HTTPException(status_code=400, detail="Product already registered")
    return crud.create_product(db=db, product=product)
