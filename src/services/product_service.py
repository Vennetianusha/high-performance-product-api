from sqlalchemy.orm import Session
from src.models.product_model import Product, ProductCreate, ProductUpdate


# -----------------------------
# CREATE
# -----------------------------
def create_product(db: Session, product_data: ProductCreate):
    new_product = Product(
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        stock_quantity=product_data.stock_quantity,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


# -----------------------------
# GET
# -----------------------------
def get_product_by_id(db: Session, product_id: str):
    return db.query(Product).filter(Product.id == product_id).first()


# -----------------------------
# UPDATE (🔥 FIXED)
# -----------------------------
def update_product(db: Session, product_id: str, product_update: ProductUpdate):
    product = get_product_by_id(db, product_id)

    if not product:
        return None

    # ✅ only update provided fields (VERY IMPORTANT)
    update_data = product_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product


# -----------------------------
# DELETE
# -----------------------------
def delete_product(db: Session, product_id: str):
    product = get_product_by_id(db, product_id)

    if not product:
        return None

    db.delete(product)
    db.commit()

    return product