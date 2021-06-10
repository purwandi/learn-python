from cleo import Application
from orator.commands.migrations import(
  InstallCommand,
  MigrateMakeCommand,
  MigrateCommand,
  RollbackCommand,
  StatusCommand,
  ResetCommand,
  RefreshCommand
)
from orator.commands.seeds import SeedersMakeCommand, SeedCommand
from orator.commands.models import ModelMakeCommand

from skeleton.cmd.rest import RestCommand
from skeleton.bootstrap import db

cli = Application('skeleton', '1.0.0')

cli.add(InstallCommand())
cli.add(MigrateMakeCommand())
cli.add(MigrateCommand(resolver=db))
cli.add(RollbackCommand(resolver=db))
cli.add(StatusCommand(resolver=db))
cli.add(ResetCommand(resolver=db))
cli.add(RefreshCommand(resolver=db))
cli.add(SeedersMakeCommand())
cli.add(SeedCommand(resolver=db))
cli.add(ModelMakeCommand())

cli.add(RestCommand())
