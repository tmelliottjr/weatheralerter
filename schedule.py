import json
from app import db
from app.apis import sms, weather
from app.models import User

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
      sms.send(phone_number, forecast)

if __name__ == '__main__':
  users = User.query.filter(User.subscribed == True).all()
  subscribers = build_subscribers(users)
  send_daily_forecast(subscribers)
