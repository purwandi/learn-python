import click

@click.command(name="db:migrate:create", help="Create database migrations")
def migrate_create():
  click.echo('create database migrations')

@click.command(name="db:migrate:up", help="Run database migrations")
def migrate_up():
  click.echo('run database migrations')

@click.command(name="db:migrate:rollback", help="Rollback database migrations")
def migrate_rollback():
  click.echo('rollback database migrations')