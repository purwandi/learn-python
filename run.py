import click

from bootstrap import app, cfg

@click.group()
def cli():
  pass

@click.command(help="Print hello world")
def hello():
  click.echo('helo')

@click.command(help="Run rest http server")
def rest():
  click.echo("rest is running")
  app.run(debug=True, host="0.0.0.0", port="8080")

@click.command(help="Print config")
def config():
  click.echo("print config")
  print(cfg.name)
  print(cfg.port)
  print(cfg.database.write)

cli.add_command(config)
cli.add_command(hello)
cli.add_command(rest)

if __name__ == '__main__':
  cli()