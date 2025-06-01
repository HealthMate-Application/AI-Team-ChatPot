from fastapi import FastAPI, Header
from pydantic import BaseModel
from Chatpot.chat_arch.chat import ChatBot, ChatBotWrapper
from Chatpot.chat_arch.memory import get_chat_history
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from typing import Optional
import uuid

app = FastAPI()

# Initialize the chatbot components
chat = ChatBot()
llm = ChatBotWrapper(chat)

system_prompt = """
You are a helpful assistant called Rafeq. 
You should remember the user's name and any other details they tell you during the conversation. 
Use these details to personalize your responses in future turns of the conversation.
"""

prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_prompt),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{query}"),
])

pipeline = prompt_template | llm

pipeline_with_history = RunnableWithMessageHistory(
    pipeline,
    get_session_history=get_chat_history,
    input_messages_key="query",
    history_messages_key="history",
)

class Message(BaseModel):
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    session_id: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    message: Message,
    x_session_id: Optional[str] = Header(None)
):
    # Use provided session_id or generate a new one
    session_id = message.session_id or x_session_id or str(uuid.uuid4())
    
    # Get response using the pipeline with history
    response = await pipeline_with_history.ainvoke(
        {"query": message.message},
        config={"session_id": session_id}
    )
    
    # Extract the content from the AIMessage
    response_content = response.content if hasattr(response, 'content') else str(response)
    
    return ChatResponse(
        response=response_content,
        session_id=session_id
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Rafeq Chat API"}


