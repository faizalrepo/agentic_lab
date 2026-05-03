from fastapi import APIRouter
from .chat import gen_res
from pydantic import BaseModel

class ChatRequest(BaseModel):
    qry: str

router = APIRouter()

@router.post("")
def chat_now (req: ChatRequest):
    print("Good start")
    return gen_res(req.qry)