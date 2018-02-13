import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'loose!lips!sink!ships'
  TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
  TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')