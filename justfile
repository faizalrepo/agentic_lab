# Run FastAPI with reload + logs
dev:
    uv run uvicorn main:app \
        --reload \
        --host 0.0.0.0 \
        --port 8000 \
        --log-level debug \
        --access-log

# Production-style run (no reload)
start:
    uv run uvicorn main:app \
        --host 0.0.0.0 \
        --port 8000