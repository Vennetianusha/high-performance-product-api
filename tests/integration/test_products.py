import pytest
import httpx
from src.main import app


@pytest.mark.asyncio
async def test_create_and_get_product():

    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        # ----------------------------
        # Create Product
        # ----------------------------
        create_response = await client.post(
            "/products/",
            json={
                "name": "Test Product",
                "description": "Test Description",
                "price": 100.0,
                "stock_quantity": 10
            }
        )

        assert create_response.status_code == 201
        created_product = create_response.json()
        product_id = created_product["id"]

        # ----------------------------
        # First GET
        # ----------------------------
        get_response_1 = await client.get(f"/products/{product_id}")
        assert get_response_1.status_code == 200

        # ----------------------------
        # Second GET
        # ----------------------------
        get_response_2 = await client.get(f"/products/{product_id}")
        assert get_response_2.status_code == 200

        assert get_response_2.json()["id"] == product_id
