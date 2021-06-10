from orator.migrations import Migration
class CreateUser(Migration):
  def up(self):
    with self.schema.create('users') as table:
      table.increments('id')
      table.string('username')
      table.timestamps()

  def down(self):
    self.schema.drop('users')
