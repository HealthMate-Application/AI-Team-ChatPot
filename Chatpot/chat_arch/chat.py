from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.outputs import ChatGeneration, ChatResult
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, BaseMessage
from typing import List, Any, Dict, Optional
from pydantic import PrivateAttr

class ChatBot:
    def __init__(self, model_name="microsoft/phi-4"):
        load_dotenv()
        self.api_key = os.getenv("MY_TOKEN")
        self.model = model_name
        self.client = InferenceClient(
            provider="nebius",
            api_key=self.api_key,
        )
    
    def get_response(self,  messages: List[dict]) -> str:
        completion = self.client.chat.completions.create(
        model=self.model,
        messages=messages
        )
        return completion.choices[0].message.content
    


class ChatBotWrapper(BaseChatModel):
    _chatbot: ChatBot = PrivateAttr()

    def __init__(self, chatbot: ChatBot):
        super().__init__()
        self._chatbot = chatbot

    @property
    def _llm_type(self) -> str:
        return "custom-chatbot"

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[Any] = None,
        **kwargs: Any,
    ) -> ChatResult:
        formatted_messages = []
        
        # Debug print to see what messages we're receiving
        print("Received messages:", messages)
        
        # Process all messages at once
        for msg in messages:
            if isinstance(msg, SystemMessage):
                formatted_messages.append({"role": "system", "content": msg.content})
            elif isinstance(msg, HumanMessage):
                formatted_messages.append({"role": "user", "content": msg.content})
            elif isinstance(msg, AIMessage):
                formatted_messages.append({"role": "assistant", "content": msg.content})
        
        print("Final formatted messages:", formatted_messages)
        response = self._chatbot.get_response(formatted_messages)

        return ChatResult(
            generations=[ChatGeneration(message=AIMessage(content=response))]
        )


if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("What is the capital of France?")
    print(response)