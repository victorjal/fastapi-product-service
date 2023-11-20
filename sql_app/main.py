from fastapi import Depends, FastAPI, HTTPException
from . import crud, models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/v1/products/create", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):    
    return crud.create_product(db=db, product=product)
