from flask import Blueprint

router = Blueprint("router", __name__, url_prefix="/api")

from api.product import *
from api.user import *