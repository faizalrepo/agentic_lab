from projects.ai_api.chat_router import router
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

app.include_router(router, prefix="/chat", tags="chat")

@app.get("/")
def root():
    return {"message": "Agentic Lab Running"}

# @app.get("/chat")
# def chat():
