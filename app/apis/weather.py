import re
import json
import requests
from app import app

base_url = 'http://api.openweathermap.org/data/'
version = '2.5'
api_url = f'{base_url}{version}/'
country = 'us'

# FIXME: reduce code duplication
# FIXME: improve validation and failure response

def get_current(zip_code):
  weather_url = f'{api_url}weather/'
  payload = {'zip': f'{zip_code},{country}', 'appid': app.config['OWM_API_KEY']}
  resp = requests.get(weather_url, params=payload)
  return resp.json()

def get_forecast(zip_code):
  forecast_url = f'{api_url}forecast/'
  payload = {'zip': f'{zip_code},{country}', 'appid': app.config['OWM_API_KEY']}
  resp = requests.get(forecast_url, params=payload)
  return resp.json()

def valid_zip_code(zip_code):
  return re.search(r'^\d{5}(?:[-\s]\d{4})?$', zip_code)