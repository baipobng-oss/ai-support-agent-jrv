from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

load_dotenv()

app = FastAPI()

# CHECK API KEY
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing")

client = OpenAI(api_key=api_key)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REQUEST MODEL
class ChatRequest(BaseModel):
    message: str

# TEST ROUTE
@app.get("/")
def root():
    return {"message": "API working"}

# HEALTH CHECK
@app.get("/health")
def health():
    return {"status": "ok"}

# CHAT ROUTE
@app.post("/chat")
async def chat(req: ChatRequest):

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": req.message
                }
            ]
        )

        return {
            "response": response.choices[0].message.content
        }

    except Exception as e:
        return {
            "error": str(e)
        }