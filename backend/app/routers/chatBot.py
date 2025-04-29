from fastapi import APIRouter
from app.chatbot.logic import processar_mensagem
from app.models.models import Mensagem
router = APIRouter()

@router.post("/chat")
def responder_mensagem(mensagem: Mensagem):
    resposta = processar_mensagem(mensagem.texto)
    return {"resposta": resposta}
