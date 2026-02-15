import uuid
from sqlalchemy import Column, String, Float, Integer
from pydantic import BaseModel
from src.database import Base


# -----------------------
# SQLAlchemy DB Model
# -----------------------
class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)


# -----------------------
# Pydantic Schemas
# -----------------------

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock_quantity: int


class ProductResponse(BaseModel):
    id: str
    name: str
    description: str
    price: float
    stock_quantity: int

    class Config:
        from_attributes = True
