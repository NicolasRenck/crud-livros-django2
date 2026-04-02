# Gerenciador de Livros / Biblioteca pessoal (CRUD)

Aplicação web para organização de biblioteca pessoal desenvolvida com Django.
Cada usuário possui sua própria lista privada, podendo gerenciar seus livros de forma individual e segura.


## Funcionalidades

Autenticação Completa: Cadastro de novos usuários e sistema de login/logout.

Gerenciamento de Livros (CRUD): Adicionar, visualizar, editar e excluir registros de livros.

Slugs Automáticos: URLs amigáveis geradas automaticamente a partir do título do livro.

Interface Minimalista: Design focado na experiência do usuário com feedback visual.

Segurança de Dados: Restrição de acesso onde um usuário não pode visualizar ou editar livros de outros.


## Tecnologias

Python 3.13 + Django 6.0.3

Django Function Based Views (FBVs).

SQLite (Banco de dados relacional).

Django Contrib Auth (Sistema de permissões e usuários).

HTML5 + CSS3 (Templates customizados).


## Screenshots
 
![Login](screenshots/login.png)

![Registro](screenshots/registro.png)

![Lista](screenshots/lista-livros.png)

![Adicionar livro](screenshots/add-livro.png)

![Editar livro](screenshots/edit-livros.png)

![Excluir livro](screenshots/delete-livro.png)

![Ver livro](screenshots/ver-livro.png)


## Como rodar localmente
```bash
git clone https://github.com/NicolasRenck/crud-livros-django2
cd crud_livros02
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


**requirements.txt:**
```
asgiref==3.11.1
Django==6.0.3
sqlparse==0.5.5
tzdata==2025.3
