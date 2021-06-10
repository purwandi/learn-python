import yaml
import io
from flask import Flask
from skeleton.bootstrap.config import Config
from skeleton.bootstrap.database import connect

app = Flask(__name__)

with io.open("config.yaml", "r") as stream:
  print("on load configuration file")
  cfg = Config(yaml.safe_load(stream))
  db = connect(cfg.database.write)

from skeleton.api import router

# register route handler
app.register_blueprint(router)

# blueprints = [
#   router
# ]
# for s in blueprints:
  # app.register_blueprint(s)
