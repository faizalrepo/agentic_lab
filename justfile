# Run FastAPI with reload + logs
dev:
    uvicorn main:app \
        --reload \
        --host 0.0.0.0 \
        --port 8000 \
        --log-level debug \
        --access-log

# Production-style run (no reload)
start:
    uvicorn main:app \
        --host 0.0.0.0 \
        --port 8000