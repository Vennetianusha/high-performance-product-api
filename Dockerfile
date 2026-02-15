# Stage 1: Builder
FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Stage 2: Runtime
FROM python:3.9-slim

WORKDIR /app

# Copy installed packages
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# 🔥 Copy executables like uvicorn
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy source code
COPY src/ ./src


EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
