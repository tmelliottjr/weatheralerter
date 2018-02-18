import re
import json
import requests
from app import app

apikey = app.config['AW_API_KEY']
base_url = 'http://dataservice.accuweather.com/{resource}/'
version = 'v1'
api_url = f'{base_url}{version}/'

# FIXME: reduce code duplication
# FIXME: improve validation and failure response

def get_daily_forecast(location_key):
  resource = 'forecasts'
  endpoint = f'daily/1day/{location_key}'
  forecast_url = f'{api_url.format(resource=resource)}{endpoint}'
  params = {'apikey': apikey}
  resp = requests.get(forecast_url, params=params)
  return resp.json()

def valid_zip_code(zip_code):
  return re.search(r'^\d{5}(?:[-\s]\d{4})?$', zip_code)

def get_location(zip_code):
  endpoint = '/postalcodes/search'
  resource = 'locations'
  location_url = f'{api_url.format(resource=resource)}{endpoint}'
  params = {'apikey': apikey, 'q': zip_code}
  resp = requests.get(location_url, params=params).json()[0] # Only ever want first/only result
  friendly_name = resp['LocalizedName']
  location_key = resp['Key']
  return (location_key, friendly_name)
  
