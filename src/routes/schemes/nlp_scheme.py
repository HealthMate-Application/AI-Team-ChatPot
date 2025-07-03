from pydantic import BaseModel

class NLPScheme(BaseModel):
    session_id: str
    message: str 