import click

from skeleton.bootstrap import app, cfg

@click.command(help="Run rest http server")
def rest():
  click.echo("rest is running")
  app.run(debug=True, host="0.0.0.0", port=cfg.port)
