from typing import List 

class Memory: 
    def __init__(self):
        self.chat_history = {}

    def get_history(self, session_id: str, template_parser, client):

        if session_id in self.chat_history.keys():
            return self.chat_history[session_id]
        
        self.chat_history[session_id] = []
        self.chat_history[session_id] = client.init_memory(mem = self.chat_history[session_id], template_parser = template_parser)

        return self.chat_history[session_id]
    

    def update(self, session_id: str, chat: List[dict]):
        self.chat_history[session_id] = chat