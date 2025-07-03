from fastapi import APIRouter, Request, FastAPI
from controllers import NLPController
from .schemes import NLPScheme
from fastapi.responses import JSONResponse

nlp_router = APIRouter()

@nlp_router.post("/chat")
async def chat(request: Request, nlp_request: NLPScheme):
    message = nlp_request.message
    session_id = nlp_request.session_id

    nlp_controller = NLPController(
        client = request.app.groq_provider, 
        template_parser=request.app.template_parser,
        memory= request.app.memory
    )
    response, session_id = nlp_controller.answer_question(message=message, session_id=session_id)
    
    return JSONResponse(
        content={
            "response": response,
            "session_id": session_id
        }
    )



