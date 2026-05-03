from google.genai.types import GenerateContentResponse
from pydantic import BaseModel
from openai import OpenAI
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

openrouter_api = os.getenv("OPENROUTER_KEY")

client = genai.Client()


def gen_res(query: str) -> str:

    response: GenerateContentResponse = client.models.generate_content(
      model="gemini-3-flash-preview",
      contents=query
    )

    return f"Got response: {response.text}"