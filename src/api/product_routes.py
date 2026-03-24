from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.product_model import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)
from src.services.product_service import (
    create_product,
    get_product_by_id,
    update_product,
    delete_product
)

from src.redis_client import (
    get_product_from_cache,
    set_product_in_cache,
    invalidate_product_cache
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# -----------------------------
# CREATE PRODUCT
# -----------------------------
@router.post("/", response_model=ProductResponse, status_code=201)
def create_new_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    created_product = create_product(db, product)

    product_response = ProductResponse.model_validate(created_product)
    set_product_in_cache(product_response)

    return product_response


# -----------------------------
# GET PRODUCT BY ID (CACHE-ASIDE)
# -----------------------------
@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: str,
    db: Session = Depends(get_db)
):
    # 1️⃣ Check cache
    cached_product = get_product_from_cache(product_id)
    if cached_product:
        print("⚡ Cache HIT")
        return cached_product

    print("❌ Cache MISS - Fetching from DB")

    # 2️⃣ DB fetch
    product = get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # 3️⃣ Store in cache
    product_response = ProductResponse.model_validate(product)
    set_product_in_cache(product_response)

    return product_response


# -----------------------------
# UPDATE PRODUCT (🔥 FIXED)
# -----------------------------
@router.put("/{product_id}", response_model=ProductResponse)
def update_existing_product(
    product_id: str,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    updated_product = update_product(db, product_id, product)

    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")

    # 🔥 invalidate cache
    invalidate_product_cache(product_id)

    return ProductResponse.model_validate(updated_product)


# -----------------------------
# DELETE PRODUCT
# -----------------------------
@router.delete("/{product_id}", status_code=204)
def delete_existing_product(
    product_id: str,
    db: Session = Depends(get_db)
):
    deleted_product = delete_product(db, product_id)

    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")

    # 🔥 invalidate cache
    invalidate_product_cache(product_id)

    return