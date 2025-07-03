from groq import Groq
from typing import List 
from ..LLMEnums import GroqEnums

class GroqProvider:
    def __init__(self, model: str, temperature:int, max_completion_tokens: int ):
        self.model = model
        self.temperature= temperature
        self.max_completion_tokens= max_completion_tokens

        self.client = Groq()


    def invoke(self, message:str, chat_history: List = []):

        chat_history.append(self.construct_prompt(text= message, role=GroqEnums.USER.value))

        ai_response = None 

        try:
            completion = self.client.chat.completions.create(
                            model=self.model,
                            messages=chat_history,
                            temperature = self.temperature,
                            max_completion_tokens = self.max_completion_tokens,
                        )
        
            ai_response = completion.choices[0].message.content
            chat_history.append(self.construct_prompt(text = ai_response, role= GroqEnums.ASSISTANT.value))
        except Exception as e:
            print(f"Streaming error: {e}")

        return ai_response, chat_history

        
        
        

    def construct_prompt(self, text:str, role:str):
        
        return {"role": role,
                "content": text}
    
    def init_memory(self, mem: List[dict], template_parser):

        mem.append({
            "role": GroqEnums.SYSTEM.value,
            "content": template_parser.get_template('rag', 'system_prompt')
        })
        return mem

        
