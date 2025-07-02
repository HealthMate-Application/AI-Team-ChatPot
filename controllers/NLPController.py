import os 
from memory import Memory


class NLPController:
    def __init__(self, client, template_parser, memory: Memory):
        self.client = client
        self.template_parser = template_parser
        self.memory = memory

    def answer_question(self, message: str, session_id: str):
        chat_history = self.memory.get_history(session_id=session_id, template_parser=self.template_parser, client = self.client)

        response, chat_history = self.client.invoke(message = message, chat_history = chat_history)
        self.memory.update(session_id=session_id, chat=chat_history)

        return response, session_id
