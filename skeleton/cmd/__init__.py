import click

from skeleton.cmd.rest import *

@click.group()
def cli():
  pass

cli.add_command(rest)
