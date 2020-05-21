from flask_restx import Api
from flask import Blueprint
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:Sidhu@9693@localhost:5432/blogs")

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.blogs_controller import api as blogs_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(blogs_ns, path="/blogs")


# The above code within blueprint.py does the following:
# In line 8, we create a blueprint instance by passing name and import_name. API is the main entry point for the application resources and hence needs to be initialized with the blueprint in line 10.
# In line 16 , we add the user namespace user_ns to the list of namespaces in the API instance.