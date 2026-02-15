from sqlalchemy.orm import Session
from src.models.product_model import Product, ProductCreate


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


def get_product_by_id(db: Session, product_id: str):
    return db.query(Product).filter(Product.id == product_id).first()


def update_product(db: Session, product_id: str, update_data: ProductCreate):
    product = get_product_by_id(db, product_id)

    if not product:
        return None

    product.name = update_data.name
    product.description = update_data.description
    product.price = update_data.price
    product.stock_quantity = update_data.stock_quantity

    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product_id: str):
    product = get_product_by_id(db, product_id)

    if not product:
        return None

    db.delete(product)
    db.commit()

    return product
