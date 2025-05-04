from datetime import datetime
from app.database import get_connection
import unicodedata

def consultar_proximo_jogo():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM jogos WHERE data > datetime("now") ORDER BY data')
    jogos = cursor.fetchall()
    conn.close()

    if jogos:
        resposta = "Próximos jogos da FURIA:\n"
        for jogo in jogos:
            data_formatada = datetime.strptime(jogo["data"], "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y")
            resposta += f"\nContra {jogo['oponente']} no dia {data_formatada} pelo {jogo['competicao']}"
        return resposta
    else:
        return "Não há jogos futuros agendados no momento."

def consultar_escalacao():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM escalacao ORDER BY nome')
    membros = cursor.fetchall()
    conn.close()

    if membros:
        resposta = "Escalação da FURIA:\n"
        for membro in membros:
            resposta += f"\nTag: {membro['nome']} Idade: {membro['idade']} Titularidade: {membro['titularidade']}"
        return resposta
    else:
        return "Não há jogadores cadastrados no momento."

def consultar_ultimo_resultado():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM resultados ORDER BY data DESC LIMIT 1')
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        return (f"Resultado da última partida:\n"
                f"\nFURIA: {resultado['resultado_furia']}"
                f"\n{resultado['nome_oponente']}: {resultado['resultado_oponente']}")
    else:
        return "Não há resultados anteriores."

def normalizar_texto(texto: str) -> str:
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower()

def processar_mensagem(texto: str) -> str:
    texto = normalizar_texto(texto)

    if ("quando " in texto and "joga " in texto) or ("qual" in texto and "jogo" in texto):
        return consultar_proximo_jogo()
    elif ("atual" in texto and "escalacao") or ("qual" in texto and "integrantes" in texto):
        return consultar_escalacao()
    elif ("resultado" in texto and "ultima") or ("ultima" in texto):
        return consultar_ultimo_resultado()
    elif "oi" in texto or "ola" in texto:
        return ("Olá! como vai furioso?\n\n"
                "Pergunte algo sobre o time de CS da Fúria!\n"
                "Pode ser sobre os próximos jogos, a escalação principal\n"
                "ou até mesmo o resultado da última partida!")
    elif "bom dia" in texto:
        return ("Bom dia! como vai furioso?\n\n"
                "Pergunte algo sobre o time de CS da Fúria!\n"
                "Pode ser sobre os próximos jogos, a escalação principal\n"
                "ou até mesmo o resultado da última partida!")
    elif "boa tarde" in texto:
        return ("Boa tarde! como vai furioso?\n\n"
                "Pergunte algo sobre o time de CS da Fúria!\n"
                "Pode ser sobre os próximos jogos, a escalação principal\n"
                "ou até mesmo o resultado da última partida!")
    elif "boa noite" in texto:
        return ("Boa noite! como vai furioso?\n\n"
                "Pergunte algo sobre o time de CS da Fúria!\n"
                "Pode ser sobre os próximos jogos, a escalação principal\n"
                "ou até mesmo o resultado da última partida!")
    elif ("o que e" in texto and "furia" in texto) or ("quem" in texto and "fundou" in texto and "furia" in texto):
        return "A FURIA é uma organização brasileira de e-sports, fundada em 2017 por Jaime Pádua e André Akkari."
    elif ("onde" in texto and "posso" in texto and "seguir" in texto) or ("qual" in texto and "instagram" in texto) or ("qual" in texto and "redes" in texto and "sociais" in texto):
        return "Você pode seguir a FURIA no Instagram (@furia) e no Twitter (@FURIA)."
    else:
        return "Desculpe furioso! Não compreendi muito bem a pergunta, poderia reformular?"