#flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()
# this file is used to solve circiular import   第三方插件