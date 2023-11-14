from sqlalchemy.orm import Session
from . import models, schemas

def create_product(db: Session, product: schemas.ProductCreate) -> models.Product:
    db_product = models.Product(
        name=product.name,
        uom=product.uom,
        category_name=product.category_name,
        is_producible=product.is_producible,
        is_purchasable=product.is_purchasable,
        type=product.type,
        additional_info=product.additional_info,
        purchase_uom=product.purchase_uom,
        purchase_uom_conversion_rate=product.purchase_uom_conversion_rate,
        batch_tracked=product.batch_tracked,
        created_at=product.created_at,
        updated_at=product.updated_at
    )
    
    for variant in product.variants:
        db_variant = models.Variant(
            sku=variant.sku,
            sales_price=variant.sales_price,
            purchase_price=variant.purchase_price,
            type=variant.type,
            created_at=variant.created_at,
            updated_at=variant.updated_at
        )
        
        for config_attribute in variant.config_attributes:
            db_config_attribute = models.ConfigAttribute(
                config_name=config_attribute.config_name,
                config_value=config_attribute.config_value
            )
            db_variant.config_attributes.append(db_config_attribute)
        
        db_product.variants.append(db_variant)
    
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    
    return db_product