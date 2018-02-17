import random
from app import app
from twilio.rest import Client

our_phone = '+17743570772'
client = Client(app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])
 
def send(phone_number, body):
  client.messages.create(from_=our_phone, to=phone_number, body=body)
  return
  