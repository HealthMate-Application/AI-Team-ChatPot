from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from llm.Providers.GroqProvider import GroqProvider
from dotenv import load_dotenv
from llm.templates import TemplateParser
from helpers.config import get_settings
from routes import nlp
from contextlib import asynccontextmanager
from memory import Memory

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    app.groq_provider = GroqProvider(
        model="compound-beta",
        temperature=0.3,
        max_completion_tokens=250,
        )

    app.template_parser = TemplateParser(
        language=settings.PRIMARY_LANG,
        default_language=settings.DEFAULT_LANG,
    )
    app.memory = Memory()

    

app = FastAPI(lifespan=lifespan)

app.include_router(nlp.nlp_router)

