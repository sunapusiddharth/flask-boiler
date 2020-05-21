from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_redis import FlaskRedis

from .config import config_by_name


# Redis intergation 


app = Flask(__name__)
app.config.from_object(config_by_name["dev"])
db = SQLAlchemy(app)
flask_bcrypt = Bcrypt(app)
redis_client = FlaskRedis(app)

print("Health check for redis :",redis_client.client_getname())