# Projeto Django Clinica

## Informações sobre o autor
**Autor:** Francisco Leite

Discente em Tecnologia em Análise e Desenvolvimento de Sistemas no IFPI

Link para a apresentação do projeto(Versão antiga): <https://www.youtube.com/watch?v=Cj-OsFUxZi4>

## Detalhamento
Nesse projeto iremos criar um sistema web com o Django para uma clínica onde os usuários poderão marcar consultas com um determinado médico de acordo com sua agenda.

## Instruções para usar esse projeto em sua máquina

1º) Clone o repositório com o seguinte comando

~~~
git clone https://github.com/NascimentoFrancisco/clinica_django.git
~~~

2º) Abra em seu editor de preferência e crie e ative o virtualenv

### Windows:
>Criação
~~~
python -m venv venv
~~~
>Ativação
~~~
venv\Scripts\activate
~~~
### Linux:
>Criação
~~~
python3 -m venv venv
~~~
>Ativação
~~~
. venv/bin/activate
~~~

3º) Isntale as dependências:

~~~
pip install -r requirements.txt
~~~

4º) Faça as migrations e o migrate:

~~~
python manage.py makemigrations
~~~

~~~
python manage.py migrate
~~~

**OBS:** Crie um super usuário para ter acesso ao django-admin

~~~
python manage.py createsuperuser
~~~

5º) Inicie o servidor e acesse o link:

~~~
python manage.py runserver
~~~

~~~
http://127.0.0.1:8000/
~~~
