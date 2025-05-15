from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Chatpot.chat_arch.chat import ChatBot
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Message(BaseModel):
    message: str


@app.post("/chat")
async def chat(message: Message):
    try:
        logger.info(f"Received message: {message.message}")
        chatbot = ChatBot()
        response = chatbot.get_response(message.message)
        logger.info(f"Generated response: {response}")
        return {"response": response}
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


