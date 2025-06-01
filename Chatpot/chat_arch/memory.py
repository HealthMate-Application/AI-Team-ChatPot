from langchain_core.chat_history import InMemoryChatMessageHistory


chat_map = {}
def get_chat_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in chat_map:
        chat_map[session_id] = InMemoryChatMessageHistory()

    return chat_map[session_id]