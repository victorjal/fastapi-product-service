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

    __table_args__ = (
        UniqueConstraint('updated_at', 'created_at', 'type', name='product_un'),
    )

class Variant(Base):
    __tablename__ = 'variants'

    id = Column(Integer, primary_key=True)
    sku = Column(String)
    sales_price = Column(Integer)
    purchase_price = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))
    type = Column(String, ForeignKey('products.type'))
    created_at = Column(DateTime, ForeignKey('products.created_at'))
    updated_at = Column(DateTime, ForeignKey('products.updated_at'))

    product = relationship('Product', backref='variants')

class ConfigAttribute(Base):
    __tablename__ = 'config_attributes'

    config_name = Column(String, primary_key=True)
    config_value = Column(String)
    variant_id = Column(Integer, ForeignKey('variants.id'))

    variant = relationship('Variant', backref='config_attributes', cascade='all, delete')
