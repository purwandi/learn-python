from cleo import Command
from skeleton.bootstrap import app, cfg, db

class RestCommand(Command):
  """
  Run http rest service

  rest
  """
  def handle(self):
    print("rest is running")
    app.run(debug=True, host="0.0.0.0", port=cfg.port, use_reloader=False)
