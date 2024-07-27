# Create Product API

This repository contains a product management API built with [FastAPI](https://fastapi.tiangolo.com/) and [PostgreSQL](https://www.postgresql.org/). The API provides a single transactional endpoint for creating products, featuring data validation using Pydantic.

## Features

- **FastAPI**: High-performance API framework for rapid development.
- **PostgreSQL**: Reliable and scalable database for product management.
- **Single Transactional Endpoint**: Create products with a single, transactional API call.
- **Pydantic Validation**: Ensures data integrity and validation for incoming requests.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/victorjal/fastapi-product-service.git
    cd fastapi-product-service
    

2. **Start the FastAPI server**:
    ```bash
    uvicorn sql_app.main:app --reload
    ```

3. Open your browser and go to `http://localhost:8000/docs` to access the API documentation.

## Usage

- **Create a Product**: Use the POST request at `/products` with the required JSON payload. The endpoint handles transactions and validation automatically.

Example request body:
```json
{
  "id": 0,
  "name": "string",
  "uom": "string",
  "category_name": "string",
  "is_producible": true,
  "is_purchasable": true,
  "type": "string",
  "purchase_uom": "string",
  "purchase_uom_conversion_rate": 0,
  "batch_tracked": true,
  "additional_info": "string",
  "created_at": "2024-07-27T20:29:35.291Z",
  "updated_at": "2024-07-27T20:29:35.291Z",
  "variants": [
    {
      "id": 0,
      "sku": "string",
      "sales_price": 0,
      "product_id": 0,
      "purchase_price": 0,
      "type": "string",
      "created_at": "2024-07-27T20:29:35.291Z",
      "updated_at": "2024-07-27T20:29:35.291Z",
      "config_attributes": [
        {
          "config_name": "string",
          "config_value": "string"
        }
      ]
    }
  ]
}

