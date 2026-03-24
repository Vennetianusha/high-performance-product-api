import uuid
from typing import Optional
from sqlalchemy import Column, String, Float, Integer
from pydantic import BaseModel, ConfigDict
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

# CREATE
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock_quantity: int


# UPDATE (🔥 important for partial update)
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock_quantity: Optional[int] = None


# RESPONSE
class ProductResponse(BaseModel):
    id: str
    name: str
    description: str
    price: float
    stock_quantity: int

    model_config = ConfigDict(from_attributes=True)