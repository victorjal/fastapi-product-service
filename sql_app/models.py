from __future__ import annotations
from datetime import datetime

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    uom: Mapped[str]
    category_name: Mapped[str]
    is_producible: Mapped[bool]
    is_purchasable: Mapped[bool]
    type: Mapped[str]
    additional_info: Mapped[str]
    purchase_uom: Mapped[str]
    purchase_uom_conversion_rate: Mapped[int]
    batch_tracked: Mapped[bool]
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

    variants: Mapped[list["Variant"]] = relationship(back_populates="product")

class Variant(Base):
    __tablename__ = 'variants'

    id: Mapped[int] = mapped_column(primary_key=True)
    sku: Mapped[str]
    sales_price: Mapped[int]
    purchase_price: Mapped[int]
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    config_attributes = Column(JSONB)

    product: Mapped["Product"] = relationship(back_populates="variants")
