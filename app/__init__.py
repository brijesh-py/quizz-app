from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key='secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"


db = SQLAlchemy(app)
migrate = Migrate()
migrate.init_app(app, db) 


from .urls import *