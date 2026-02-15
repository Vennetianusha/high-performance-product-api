# 🚀 High-Performance Product API with Redis Caching

> A production-ready backend system implementing **Cache-Aside strategy** using Redis to optimize performance for data-intensive applications.

---

## 📌 Project Overview

This project demonstrates how to build a scalable backend API that minimizes database load and improves response time using intelligent Redis caching.

It implements:

- ⚡ FastAPI for RESTful API design  
- 🗄 SQLite for persistent storage  
- 🔥 Redis for high-speed caching  
- 🧠 Cache-Aside strategy  
- 🐳 Docker & Docker Compose for containerization  
- 🧪 Automated integration testing  

---

## 🏗 Architecture

Client
↓
FastAPI (API Layer)
↓
Redis (Cache Layer)
↓
SQLite (Persistent Database)


---

## 🧠 Caching Strategy — Cache-Aside Pattern

### 🔍 Read Operation (GET /products/{id})

1. Check Redis cache first  
2. If cache HIT → return cached data  
3. If cache MISS → fetch from database  
4. Store result in Redis with TTL  
5. Return response  

### ✏ Write Operations (POST / PUT / DELETE)

1. Update database first  
2. Invalidate Redis cache entry  
3. Ensure next GET fetches fresh data  

This ensures **data consistency** and **high performance**.

---

## ✨ Features

- ✅ Full CRUD operations
- ✅ Intelligent Redis caching
- ✅ Cache invalidation on updates
- ✅ Configurable TTL
- ✅ Graceful Redis fallback
- ✅ Dockerized multi-container setup
- ✅ Clean layered architecture
- ✅ Automated integration tests

---

## 📂 Project Structure

my-product-api/
│
├── src/
│ ├── api/
│ ├── services/
│ ├── models/
│ ├── main.py
│ ├── database.py
│ └── redis_client.py
│
├── tests/
│ └── integration/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
└── README.md


---

## 🐳 Run with Docker (Recommended)

### 🔨 Build & Start

```bash
docker compose up --build
🌐 Access API
http://localhost:8080/docs
Interactive Swagger UI will be available.

🧪 Run Tests
🔹 Locally
pytest
🔹 Inside Docker
docker compose exec api-service pytest
🔥 API Endpoints
Method	Endpoint	Description
POST	/products	Create product
GET	/products/{id}	Get product (cached)
PUT	/products/{id}	Update product
DELETE	/products/{id}	Delete product
GET	/health	Health check
⚙ Environment Variables
Variable	Description
API_PORT	API listening port
REDIS_HOST	Redis service host
REDIS_PORT	Redis port
CACHE_TTL_SECONDS	Cache expiration time
DATABASE_URL	Database connection string
📈 Demonstrating Cache Behavior
Create product

First GET → Cache MISS

Second GET → Cache HIT

Update product → Cache invalidated

Next GET → Cache MISS again

🧑‍💻 Technologies Used
Python

FastAPI

Redis

SQLAlchemy

SQLite

Pytest

Docker

Docker Compose

🎯 Key Design Decisions
Used Cache-Aside pattern for simplicity and scalability

Implemented cache invalidation to prevent stale data

Multi-stage Docker build for optimized image size

Clean separation of API, service, and data layers

🚀 Why This Project Matters
This project demonstrates:

Backend performance optimization

Real-world caching strategies

Containerized microservice architecture

Production-ready coding practices

👩‍💻 Author
Anusha Pavani Venneti
