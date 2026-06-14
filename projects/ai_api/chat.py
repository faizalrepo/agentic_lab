from google.genai.types import GenerateContentResponse
from pydantic import BaseModel
from openai import OpenAI
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

openrouter_api = os.getenv("OPENROUTER_KEY")

client = genai.Client()

class Response(BaseModel):
    response: str


def gen_res(query: str) -> dict:

    response: GenerateContentResponse = client.models.generate_content(
      model="gemini-3.5-flash",
      contents=query
    )

    # return f"Got response: {response.text}"
    return Response(response=response.text)