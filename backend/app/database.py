import sqlite3

def get_connection():
    conn = sqlite3.connect('../furia_chatbot.db')
    conn.row_factory = sqlite3.Row  # Retorna dicionários em vez de tuplas
    return conn
