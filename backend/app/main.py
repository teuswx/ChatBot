from fastapi import FastAPI
from app.routers import chatBot
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="Chatbot da FURIA",
    description="Um chatbot para responder perguntas sobre o time de CS:GO FURIA.",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # ou ["*"] durante desenvolvimento
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatBot.router)
