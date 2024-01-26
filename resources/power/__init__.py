from flask_smorest import Blueprint

bp = Blueprint ('powers', __name__, description='Ops on Powers', url_prefix='/powerl')

from . import routes