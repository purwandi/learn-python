from skeleton.bootstrap import db
from peewee import *

class BaseModel(Model):
  class Meta:
    database = db

class User(BaseModel):
  username = TextField()
  created_at = TimestampField()
  updated_at = TimestampField()

  class Meta:
    table_name = 'users'
    sorted_fields = []
    table_settings = None
