from groq import Groq

class GroqProvider:
    def __init__(self, model: str, temperature:int, max_completion_tokens: int , stream: bool):
        self.model = model
        self.temperature= temperature
        self.max_completion_tokens= max_completion_tokens
        self.stream= stream
        self.chat_history=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        ]

        self.client = Groq()


    def invoke(self, message:str):

        self.chat_history.append(self.construct_prompt(text= message, role="user"))

        ai_res = ""

        completion = self.client.chat.completions.create(
                        model=self.model,
                        messages=self.chat_history,
                        temperature = self.temperature,
                        max_completion_tokens = self.max_completion_tokens,
                        stream= self.stream)
        
        try:
            list_of_tools = []
            for chunk in completion:
                ai_response = chunk.choices[0].delta.content
                tool = chunk.choices[0].delta.executed_tools
                if tool not in list_of_tools:
                    list_of_tools.append(tool)
                
                if ai_response:
                    ai_res += str(ai_response)
                    yield ai_response
        except Exception as e:
            print(f"Streaming error: {e}")
            yield "[Error occurred during streaming]"

        
        
        

    def construct_prompt(self, text:str, role:str):
        return {"role": role,
                "content": text}

        
