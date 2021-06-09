import click
from peewee_migrate import Router
from bootstrap import db

migrator = Router(db)

@click.command(name="db:migrate:create", help="Create database migrations")
@click.argument('name')
@click.argument('table', required=False)
def migrate_create(name, table):
  migrator.create(name)

@click.command(name="db:migrate:up", help="Run database migrations")
def migrate_up():
  migrator.run()

@click.command(name="db:migrate:rollback", help="Rollback database migrations")
@click.argument('name', required=False)
@click.option('--count', required=False, default=1, type=int, help="Number of last migrations to be rolled back. Ignored in case of non-empty name")
def migrate_rollback(name, count):
  if not name:
    if len(migrator.done) < count:
      raise RuntimeError('Unable to rollback %s migrations from %s: %s' % (count, len(migrator.done), migrator.done))
    for _ in range(count):
      name = migrator.done[-1]
      migrator.rollback(name)
  else:
    migrator.rollback(name)