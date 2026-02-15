import redis
import json
from src.config import REDIS_HOST, REDIS_PORT, CACHE_TTL_SECONDS
from src.models.product_model import ProductResponse


try:
    redis_client = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        decode_responses=True
    )
    redis_client.ping()
    print("✅ Connected to Redis")
except Exception as e:
    print("⚠️ Redis connection failed:", e)
    redis_client = None


def get_product_from_cache(product_id: str):
    if not redis_client:
        return None

    try:
        cached_data = redis_client.get(product_id)
        if cached_data:
            return ProductResponse.model_validate_json(cached_data)
        return None
    except Exception:
        return None


def set_product_in_cache(product: ProductResponse):
    if not redis_client:
        return

    try:
        redis_client.setex(
            product.id,
            CACHE_TTL_SECONDS,
            product.model_dump_json()
        )
    except Exception:
        pass


def invalidate_product_cache(product_id: str):
    if not redis_client:
        return

    try:
        redis_client.delete(product_id)
    except Exception:
        pass
