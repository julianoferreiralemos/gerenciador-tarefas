# Gerenciador de Tarefas

Este projeto é um backend de um gerenciador de tarefas desenvolvido com **Django** e **Django Rest Framework**.

A ideia do projeto é criar uma API que permita que usuários possam criar, visualizar, atualizar e concluir tarefas.

Neste momento o projeto está focado apenas no **backend**. Ainda não existe frontend.

---

## Tecnologias utilizadas

* Python
* Django
* Django Rest Framework
* PostgreSQL

---

## Estrutura do projeto

O backend está organizado utilizando uma pasta `apps`, onde cada parte do sistema fica separada em sua própria aplicação.

```
backend
 ├── apps
 │   ├── core
 │   └── tasks
 ├── config
 └── manage.py
```

### core

Aplicação responsável por componentes reutilizáveis do sistema.

Atualmente contém um **BaseModel**, que centraliza campos comuns utilizados em outros modelos:

* `created_at`
* `updated_at`
* `is_active`

Esse modelo é **abstrato** e serve como base para outros modelos do projeto.

---

### tasks

Aplicação responsável pelo gerenciamento de tarefas.

O modelo `Task` possui:

* título
* descrição
* status de conclusão
* data de conclusão
* relação com usuário
* herança do `BaseModel`

Também foi criado um **TaskManager**, responsável por consultas personalizadas como:

* tarefas concluídas
* tarefas pendentes
* tarefas ativas

---

## Banco de dados

O projeto utiliza **PostgreSQL**.

As migrations do Django estão sendo usadas para controlar a estrutura do banco.

---

## Estado atual do projeto

Até o momento foram implementados:

* Estrutura modular utilizando apps
* Configuração do PostgreSQL
* Modelo de tarefas
* BaseModel reutilizável
* Manager customizado para consultas de tarefas
* Sistema de migrations funcionando

A API REST ainda será implementada nas próximas etapas.

---

## Próximos passos

* Criar serializers com Django Rest Framework
* Implementar endpoints da API
* Adicionar autenticação
* Criar frontend para consumir a API
