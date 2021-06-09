import yaml
import io
from flask import Flask
from bootstrap.config import Config
# from peewee import *
from playhouse.db_url import connect

with io.open("config.yaml", "r") as stream:
  print("on load configuration file")
  cfg = Config(yaml.safe_load(stream))
  app = Flask(__name__)
  db = connect(cfg.database.write)

from api import router

# register route handler
app.register_blueprint(router)

# blueprints = [
#   router
# ]
# for s in blueprints:
  # app.register_blueprint(s)
