from flask import Flask
import config
from extensions import db,mail
from models import UserModel
from blueprints.qa import  bp as qa_bp
from blueprints.auth import  bp as auth_bp
from flask_migrate import Migrate


app = Flask(__name__)
#bind configuration file     ...  app.config['SQLALCHEMY_DATABASE_URI']
app.config.from_object(config)


db.init_app(app)
mail.init_app(app)

migrate = Migrate(app,db)

# flask db init    migrate(modify the schema of the table)

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run()
# without this , we would have to use :flask  run --debug