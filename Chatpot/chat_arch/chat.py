# chat.py   

from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

class ChatBot:
    def __init__(self, model_name="microsoft/phi-4"):
        load_dotenv()
        self.api_key = os.getenv("MY_TOKEN")
        self.model = model_name
        self.client = InferenceClient(
            provider="nebius",
            api_key=self.api_key,
        )
    
    def get_response(self, message):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ],
        )
        return completion.choices[0].message.content

# Example usage
if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("What is the capital of France?")
    print(response)