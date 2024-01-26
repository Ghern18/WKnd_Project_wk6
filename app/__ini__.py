from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from models.xmen_model import XmenModel
from models.PowerModel import PowerModel

from resources.xmen import bp as xmen_bp
api.register_blueprint(xmen_bp)

from resources.power import bp as power_bp
api.register_blueprint(power_bp_bp)

#Missing a __pyache__ need to insert/download!