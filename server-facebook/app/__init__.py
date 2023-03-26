from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

from flask_login import LoginManager
login = LoginManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.app_context().push()

from app import routes
from app import models