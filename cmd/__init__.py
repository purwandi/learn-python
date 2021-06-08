import click

from cmd.migration import *
from cmd.rest import *

@click.group()
def cli():
  pass

cli.add_command(rest)
cli.add_command(migrate_create)
cli.add_command(migrate_up)
cli.add_command(migrate_rollback)