from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import views, api_views, errors_handlers  # noqa
