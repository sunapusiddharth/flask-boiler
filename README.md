# flask-boiler
noiler plate for flask rest app with swagger,auth using jwt ,postgres

Steps:
clone this repo
activate virtaulenv :
pip3 install --upgrade pip setuptools wheel  : installs tools for setup use pip if on python version 2.
cd into the project structire
pip3 install virtualenv
python3 -m venv env   - to setup virtual env 
env/Scripts/activate - to activate venv
You will see that the prompt of the command-line tool gets a prefix of the project
name, as follows:
(env)$
To get out of the virtual environment, type the following command
(env)$ deactivate
to install dependencies :
pip install -r requirements.txt

in anytime to freeze the requirements : pip freeze > requirements.txt
to run all test :
python manage.py test
to run the migrations
python manage.py db init
python manage.py db migrate
python manage.py db upgrade


to run the ap:
python manage.py run

go to http://localhost:5000/
check the swagger doc for list of API's
Create a  user using post method of user group api's
then login using the email id and password.
POST http://127.0.0.1:5000/auth/login {
  "email": "user1@gmail.com",
  "password": "user1"
}

copy the bearer token 
open a new tab in postman :
GET http://127.0.0.1:5000/blogs 
Add authorization as BearerToken and paste in the token copied.



to Create a new endpoint:
create a model,controller,service and swagger doc in dto.py  and initailize it in __init__.py of root of app.
Model : stores the database structure.
Controller stores the api endpoints 
Service : all business logic goes inside it.
