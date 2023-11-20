from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from ..models import Base
from ..main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_product():
    response = client.post(
        "/v1/products/create/",
        json={
                "id": 1,
                "name": "Standard-hilt lightsaber",
                "uom": "pcs",
                "category_name": "lightsaber",
                "is_producible": True,
                "is_purchasable": True,
                "type": "product",
                "purchase_uom": "pcs",
                "purchase_uom_conversion_rate": 1,
                "batch_tracked": False,
                "variants": [
                    {
                        "id": 1,
                        "sku": "EM",
                        "sales_price": 40,
                        "product_id": 1,
                        "purchase_price": 0,
                        "type": "product",
                        "created_at": "2020-10-23T10:37:05.085Z",
                        "updated_at": "2020-10-23T10:37:05.085Z",
                        "config_attributes": [
                            {
                                "config_name": "Type",
                                "config_value": "Standard"
                            }
                        ]
                    }
                ],
                "additional_info": "additional info",
                "created_at": "2020-10-23T10:37:05.085Z",
                "updated_at": "2020-10-23T10:37:05.085Z"
            },
    )
    assert response.status_code == 200