# Gerenciador de Tarefas API

API backend para gerenciamento de tarefas com autenticação JWT, construída com **Django** e **Django REST Framework**.

O projeto permite que usuários:
- Criem conta
- Façam login com JWT
- Criem, visualizem, editem e excluam tarefas

---

##  Tecnologias

- Python 3.12  
- Django 5  
- Django REST Framework  
- PostgreSQL  
- JWT Authentication (Simple JWT)  
- Docker & docker‑compose  
- drf‑spectacular (Swagger)

---

##  Funcionalidades

- Registro de usuário  
- Login com JWT  
- Refresh token  
- Dados do usuário autenticado  
- CRUD de tarefas  
- Busca e filtro de tarefas  
- Paginação automática

---

##  Estrutura


backend
├── apps
│ ├── accounts
│ ├── core
│ └── tasks
├── config
└── manage.py


- `accounts`: lógica de autenticação  
- `tasks`: endpoints de tarefas  
- `core`: utilitários globais  
- `config`: configurações do Django

---

##  Como rodar

### 🔹 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/gerenciador-de-tarefas.git
cd gerenciador-de-tarefas/backend
🔹 2. Criar .env

Crie um arquivo .env com as variáveis:

SECRET_KEY=django-insecure-dev-key
DEBUG=True

DB_NAME=tasksdb
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
🔹 3. Com Docker (recomendado)
docker compose up --build

A API estará em:
 Swagger: http://127.0.0.1:8000/api/docs/
 Admin: http://127.0.0.1:8000/admin/

🔹 4. Sem Docker
python -m venv venv
source venv/bin/activate      # Linux/WSL
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
 Endpoints principais
 Autenticação
Método	Rota	Descrição
POST	/api/auth/register	Registrar usuário
POST	/api/auth/login	Login com JWT
POST	/api/auth/refresh	Refresh token
GET	/api/auth/me	Detalhes do usuário
 Tarefas
Método	Rota	Descrição
GET	/api/tasks	Lista tarefas
POST	/api/tasks	Cria tarefa
GET	/api/tasks/{id}	Detalha tarefa
PUT	/api/tasks/{id}	Atualiza tarefa
DELETE	/api/tasks/{id}	Exclui tarefa

Todos endpoints de tarefas exigem JWT válido.

 Observações finais

 Backend funcional e pronto para ser usado
 Swagger configurado para exploração da API


 Status

Status:  Completo (backend com autenticação, documentação e Docker)