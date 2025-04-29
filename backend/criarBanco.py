import sqlite3

conn = sqlite3.connect('furia_chatbot.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS jogos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        oponente TEXT NOT NULL,
        data TEXT NOT NULL,
        competicao TEXT NOT NULL
               )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS escalacao(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        titularidade TEXT NOT NULL
               )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS resultados(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resultado_furia INTEGER NOT NULL,
        resultado_oponente INTEGER NOT NULL,
        nome_oponente TEXT NOT NULL,
        data TEXT NOT NULL
               )
''')

cursor.execute('''
    INSERT INTO jogos(oponente, data, competicao) VALUES
        ('Natus Vincere', '2025-05-07 18:00:00', 'IEM Rio 2024'),
        ('Virtus.pro', '2025-05-10 14:00:00', 'IEM Rio 2024')
''')

cursor.execute('''
    INSERT INTO escalacao(nome, idade, titularidade) VALUES
        ('MOLODOY', 20, 'Titular'),    
        ('YEKINDAR', 25, 'Titular'),    
        ('FalleN', 33, 'Titular'),    
        ('KSCERATO', 25, 'Titular'),    
        ('yuurih', 25, 'Titular'),    
        ('skullz', 23, 'Reserva'),    
        ('chelo', 26, 'Reserva')      
    ''')

cursor.execute('''
    INSERT INTO resultados(resultado_furia, resultado_oponente, nome_oponente, data) VALUES
        (0, 2, 'TheMongolz', '2025-04-09 09:50:00'),
        (0, 2, 'Virtus.pro', '2025-04-08 06:05:00')
''')

conn.commit()
conn.close()