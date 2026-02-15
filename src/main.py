from fastapi import FastAPI
from src.database import engine, Base
from src.api.product_routes import router as product_router

# Create FastAPI instance
app = FastAPI(title="High-Performance Product API with Redis Caching")

# Create tables in database
Base.metadata.create_all(bind=engine)

# Include product routes
app.include_router(product_router)


@app.get("/")
def read_root():
    return {"message": "Product API is running successfully 🚀"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
