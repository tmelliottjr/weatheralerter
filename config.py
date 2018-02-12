import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'loose!lips!sink!ships'