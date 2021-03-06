#!/var/www/weatheralerter/venv/bin/python

import json
from app import db
from app.apis import sms, weather
from app.models import User
import twilio

def build_subscribers(users):
  subscribers = {}

  for user in users:
    try:
      subscribers[user.zip_code].append(user.phone_number)
    except KeyError:
      subscribers[user.zip_code]=[user.phone_number]
  
  return subscribers

def get_forecast(zip_code):
  forecast = weather.Forecast()
  forecast.location_from_postal_code(postal_code=zip_code)
  forecast.get_forecast()

  return forecast.formatted_forecast()

def send_daily_forecast(subscribers):
  for zip_code, phone_numbers in subscribers.items():
    forecast = get_forecast(zip_code)   

    for phone_number in phone_numbers:
      try:
        sms.send(phone_number, forecast)
      except twilio.base.exceptions.TwilioRestException as e:
        print(f'{phone_number}:\n', e)
      
if __name__ == '__main__':
  users = User.query.filter(User.phone_number == '4019652591').all()
  subscribers = build_subscribers(users)
  send_daily_forecast(subscribers)
