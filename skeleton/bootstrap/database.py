from urllib.parse import parse_qsl, unquote, urlparse
from orator import DatabaseManager

def parseresult_to_dict(parsed, unquote_password=False):
  path_parts = parsed.path[1:].split('?')
  try:
    query = path_parts[1]
  except IndexError:
    query = parsed.query

  connect_kwargs = {'database': path_parts[0]}
  if parsed.username:
    connect_kwargs['user'] = parsed.username
  if parsed.password:
    connect_kwargs['password'] = parsed.password
    if unquote_password:
      connect_kwargs['password'] = unquote(connect_kwargs['password'])
  if parsed.hostname:
    connect_kwargs['host'] = parsed.hostname
  if parsed.port:
    connect_kwargs['port'] = parsed.port

  # Adjust parameters for MySQL.
  if parsed.scheme == 'mysql' and 'password' in connect_kwargs:
    connect_kwargs['passwd'] = connect_kwargs.pop('password')
  elif 'sqlite' in parsed.scheme and not connect_kwargs['database']:
    connect_kwargs['database'] = ':memory:'

  # driver
  if parsed.scheme == "postgresql":
    connect_kwargs['driver'] = "postgres"

  # Get additional connection args from the query string
  qs_args = parse_qsl(query, keep_blank_values=True)
  for key, value in qs_args:
    if value.lower() == 'false':
      value = False
    elif value.lower() == 'true':
      value = True
    elif value.isdigit():
      value = int(value)
    elif '.' in value and all(p.isdigit() for p in value.split('.', 1)):
      try:
        value = float(value)
      except ValueError:
        pass
    elif value.lower() in ('null', 'none'):
      value = None

    connect_kwargs[key] = value

  return connect_kwargs

def connect(url, unquote_password=False):
  parsed = urlparse(url)
  database = {
    'default': 'postgres',
    'postgres': parseresult_to_dict(parsed, unquote_password)
  }

  print('database initialize')

  return DatabaseManager(database)
