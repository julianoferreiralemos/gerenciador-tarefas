# Gerenciador de Tarefas - API Django

API backend profissional para gerenciamento de tarefas, desenvolvida com **Django** e **Django REST Framework**.  
Permite que usuários criem contas, façam login com JWT e gerenciem suas próprias tarefas.

---

# Tecnologias

- Python 3.12  
- Django 5  
- Django REST Framework  
- PostgreSQL  
- JWT Authentication (Simple JWT)  
- Docker & Docker Compose  
- drf-spectacular (Swagger / OpenAPI)

---

# Funcionalidades

- Registro de usuário  
- Login com JWT  
- Refresh token  
- Dados do usuário autenticado  
- CRUD de tarefas  
- Filtro de tarefas  
- Busca de tarefas  
- Paginação automática  

---

# Estrutura do projeto


backend
├── apps
│ ├── core
│ ├── tasks
│ └── accounts
├── config
└── manage.py


- **apps/** → aplicações modulares (tarefas, contas, core)  
- **config/** → configurações globais do Django (settings, urls, wsgi)  

---

# Rodando o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/gerenciador-de-tarefas.git
cd gerenciador-de-tarefas/backend
2. Configure variáveis de ambiente

Crie um arquivo .env na raiz do backend com as seguintes variáveis:

SECRET_KEY=django-insecure-dev-key
DEBUG=True

DB_NAME=tasksdb
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
3. Com Docker (recomendado)
docker compose up --build

Acesse:

Admin: http://127.0.0.1:8000/admin/

Swagger / OpenAPI: http://127.0.0.1:8000/api/docs/

4. Sem Docker
python -m venv venv
source venv/bin/activate  # Linux / WSL
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Endpoints principais
Autenticação

POST /api/auth/register → registra novo usuário

POST /api/auth/login → login com JWT

POST /api/auth/refresh → refresh token

GET /api/auth/me → dados do usuário autenticado

Tarefas

GET /api/tasks → lista tarefas

POST /api/tasks → cria tarefa

GET /api/tasks/{id} → detalha tarefa

PUT /api/tasks/{id} → atualiza tarefa

DELETE /api/tasks/{id} → remove tarefa

Todos os endpoints de tarefas requerem autenticação JWT.

Status do projeto

Backend completo e funcional

Autenticação JWT implementada

Swagger / OpenAPI configurado

Estrutura modular pronta para expansão

Frontend ainda não implementado

Observações

JWT Authentication habilitada

Banco PostgreSQL rodando dentro do Docker ou localmente

Estrutura modular (apps/) permite adicionar novas apps facilmente