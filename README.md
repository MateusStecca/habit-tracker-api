Habit Tracker API 🚀

Uma API RESTful simples e eficiente para rastreamento de hábitos diários, construída com Python e FastAPI.

Este projeto foi criado como parte de um portfólio de desenvolvimento backend para demonstrar a criação de endpoints rápidos, documentação automática e integração com banco de dados.

🛠️ Tecnologias Utilizadas

Python

FastAPI: Framework web super rápido e moderno.

SQLite: Banco de dados leve e embutido.

SQLAlchemy: ORM para comunicação com o banco de dados.

Pydantic: Para validação de dados.

Uvicorn: Servidor para rodar a aplicação.

⚙️ Como Rodar Localmente

Clone este repositório:

git clone https://github.com/MateusStecca/habit-tracker-api.git


Crie um ambiente virtual e ative-o:

python -m venv venv
# No Windows:
venv\Scripts\activate


Instale as dependências:

pip install -r requirements.txt


Inicie o servidor:

uvicorn main:app --reload


📄 Documentação da API

Uma das grandes vantagens do FastAPI é a geração automática de documentação. Com o servidor rodando localmente, basta acessar no seu navegador:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Lá você poderá testar diretamente as rotas de Criação (POST), Listagem (GET) e Exclusão (DELETE) de hábitos.