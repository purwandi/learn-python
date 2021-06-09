from flask import Blueprint

router = Blueprint("router", __name__, url_prefix="/api")

from skeleton.api.product import *
from skeleton.api.user import *
