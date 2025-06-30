from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from llm.GroqProvider import GroqProvider
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
groq_provider = GroqProvider(
    model="compound-beta",
    temperature=0.3,
    max_completion_tokens=250,
    stream= True
    )

@app.post("/chat")
async def chat(message: str):
    return StreamingResponse(groq_provider.invoke(message), media_type="text/plain")



