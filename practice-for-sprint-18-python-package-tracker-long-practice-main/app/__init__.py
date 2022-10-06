from flask import Flask, render_template
from flask_migrate import Migrate
from .config import Config
from app import routes
from .models import db

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(routes.bp)
db.init_app(app)
migrate = Migrate(app, db)
