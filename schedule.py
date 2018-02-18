import json
from app import db
from app.apis import sms, weather
from app.models import User


# for subscriber, v in subscribers.items():
#   print(subscriber, v)

users = User.query.filter(User.subscribed == True).all()

subscribers = {}

for user in users:
  try:
    subscribers[user.zip_code].append(user.phone_number)
  except KeyError:
    subscribers[user.zip_code]=[user.phone_number]

for zip_code, phone_numbers in subscribers.items():
  current_weather = weather.get_current(zip_code)
  location = current_weather['name']
  # print('high temp:' current_weather[''])
  body = f'Current conditions in {location}:\n'
  body += 'test'
  print(body)

  # for phone_number in phone_numbers:
    # body = 'Current weather conditions in'
    # sms.send(phone_number, body)




