# Config class definition
class Config:
  def __init__(self, raw):
    self.name = raw['name']
    self.env = raw['env']
    self.port = raw['port']
    self.database = DatabaseConfig(raw['database'])

class AppConfig:
  def __init__(self, raw):
    self.name = raw['name']
    self.port = raw['port']
    self.env  = raw['env']

class DatabaseConfig:
  def __init__(self, raw):
    self.write = raw['write']
    self.read  = raw['read']

