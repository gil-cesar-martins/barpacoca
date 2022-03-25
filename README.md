# barpacoca
Django Framework Project

Aplicativo web de divulgação de um bar fictício.

### Deploy local 
Instale as seguinte bibliotecas com o comando pip:

`pip install django==4.0.2 psycopg2-binary gunicorn dj-static django-stdimage dj-database-url progressbar2 pytz six django-adminlte2`

Instale as dependências no **requirements.txt**:
 
`pip freeze > requirements.txt`

No terminal de seu ambiente de desenvolvimento, crie o projeto com: 

`django-admin startproject <nome_do_seu_projeto .`

Crie o diretório da aplicação com:
`django-admin startapp core`
 
Exporte um ENVIRONMENT para definir o banco de dados para o teste
 
`export ENVIRONMENT == 'test'`
 
Qualquer alteração nos **models** deve ser concluída com o comando:
 
`python manage.py makemigrations`
 
E depois migrar os **models** para o banco de dados:
 
`python manage.py migrate`
 
Crie um superusuário para o gerenciamento do banco de dados:
 
`python manage.py createsuperuser`
 
Execute sua aplicação:
 
`python manage.py runserver`
 
Para acessar vá no seu navegador e  digite [http://localhost:8000](http://localhost:8000)
