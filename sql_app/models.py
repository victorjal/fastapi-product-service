from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    name = Column(String)
    uom = Column(String)
    category_name = Column(String)
    id = Column(Integer, primary_key=True)
    is_producible = Column(Boolean)
    is_purchasable = Column(Boolean)
    type = Column(String)
    additional_info = Column(String)
    purchase_uom = Column(String)
    purchase_uom_conversion_rate = Column(Integer)
    batch_tracked = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    variants = relationship('Variant', backref='products')

class Variant(Base):
    __tablename__ = 'variants'

    id = Column(Integer, primary_key=True)
    sku = Column(String)
    sales_price = Column(Integer)
    purchase_price = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))

    products = relationship('Product', backref='variants', foreign_keys=[product_id])
    config_attributes = relationship('ConfigAttribute', backref='variants')

class ConfigAttribute(Base):
    __tablename__ = 'config_attributes'

    config_name = Column(String)
    config_value = Column(String)
    variant_id = Column(Integer, ForeignKey('variants.id'))
    id = Column(Integer, primary_key=True)

    variants = relationship('Variant', backref='config_attributes', cascade='all, delete', foreign_keys=[variant_id])
