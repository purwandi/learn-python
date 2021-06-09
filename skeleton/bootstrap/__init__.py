import yaml
import io
from flask import Flask
from skeleton.bootstrap.config import Config
from masoniteorm.connections import ConnectionResolver

with io.open("config.yaml", "r") as stream:
  print("on load configuration file")
  cfg = Config(yaml.safe_load(stream))
  app = Flask(__name__)


from skeleton.api import router

# register route handler
app.register_blueprint(router)

# blueprints = [
#   router
# ]
# for s in blueprints:
  # app.register_blueprint(s)
