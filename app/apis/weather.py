import re
from pyccuweather.connector import Connection

# FIXME: reduce code duplication
# FIXME: improve validation and failure response

class Forecast(object):
  def __init__(self):
    self.conn = Connection(api_type='dataservice')

  def location_from_postal_code(self, country_code='us', postal_code=None):
    if postal_code is None:
      raise ValueError('Missing postal code')
    
    if not self.valid_postal_code(postal_code):
      raise ValueError('Invalid postal code')
    
    self.location = self.conn.loc_postcode(country_code, postal_code)
    
    return self.location

  def valid_postal_code(self, postal_code):
    return re.search(r'^\d{5}(?:[-\s]\d{4})?$', postal_code)

  def get_forecast(self, type='1d', lkey=None):
    
    if lkey is None:
      try:
        lkey = self.location.lkey
      except AttributeError:
        raise ValueError('Location key required')
    
    self.forecast = self.conn.get_forecast(type, lkey=self.location.lkey, metric=False)

    return self.forecast
  
  def formatted_forecast(self):
    if self.forecast is None:
      raise ValueError('Forecast required')

    if self.location is None:
      raise ValueError('Location required')
        
    # One day forecasts only
    for k in self.forecast.forecasts:
      min = self.forecast.forecasts[k].temp_min.F
      max = self.forecast.forecasts[k].temp_max.F

    for k in self.forecast.forecasts:
      day_synopsis = self.forecast.forecasts[k].day.phrase

    deg = u'\N{DEGREE SIGN}'
    formatted = f'{self.location.localized_name}:\nHigh: {max:.2f}{deg}\nLow: {min:.2f}{deg}\n{day_synopsis}'

    return formatted
  
