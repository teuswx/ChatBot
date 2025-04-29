# Chatbot Furia ✅

## Índice
- [Descrição](#descrição)
- [Demonstração](#demonstração)
- [Tecnologias](#tecnologias)
- [Como Executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Autor](#autor)

## Descrição

O objetivo deste projeto é construir um chatbot dinâmico que atualiza as mensagens conforme o banco de dados.

A aplicação é dividida em:
- **Backend**: Gerencia as mensagens usando FastAPI e armazena dados em SQLite.
- **Frontend**: Oferece uma interface web amigável utilizando Vue.js.

---

## Demonstração

![Image](https://github.com/user-attachments/assets/a9ec952d-4124-4159-bbfb-19eebd9cba23)

## Tecnologias

### Backend
- Python 3.11+
- FastAPI
- Uvicorn
- SQLite
- SQLAlchemy

### Frontend
- Vue.js 3
- Vite
- Axios

---

## Como Executar

### Backend

```bash
# 1. Certifique-se de que o Python esteja instalado.
# 2. Entre na pasta backend:
cd backend

# 3. Crie um ambiente virtual:
python -m venv venv

# 4. Ative o ambiente virtual:
# No Windows:
.\venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

# 5. Instale as dependências:
pip install -r requirements.txt

# 6. (Opcional) Crie o banco de dados local:
python criarBanco.py

# 7. Entre na pasta principal da aplicação:
cd app

# 8. Inicie o servidor FastAPI:
uvicorn main:app --reload

```

## Frontend
```bash
# 1. Certifique-se de que o Node.js esteja instalado.
# 2. Entre na pasta frontend:
cd frontend

# 3. Instale as dependências:
npm install

# 4. Inicie o servidor de desenvolvimento:
npm run dev

# 5. Acesse a aplicação no navegador, geralmente em http://localhost:5173

```

## Estrutura do Projeto

```bash

Chatbot-Furia/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── ... (outros arquivos)
│   ├── criarBanco.py
│   ├── furia_chatbot.db (gerado após criar o banco)
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── App.vue
│   │   └── ... (outros arquivos)
│   ├── package.json
│
├── README.md

```

## Autor

| Nome | GitHub | Contato |
|:-----|:-------|:--------|
| Mateus Henrique Pereira | [@teuswx](https://github.com/teuswx) | mateushenriquepereira02@gmail.com |
