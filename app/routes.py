from flask import render_template, request, jsonify, Response
from app import app
from app.apis import sms, weather

# FIXME: better validation and failure response

# subscribe to service
@app.route('/subscribe', methods=['POST'])
def subscribe():
  return jsonify({'message': 'success'})

# unsubscribe from service
@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
  return jsonify({'message':'success'})

# get current weather for zip code
@app.route('/weather/current/<zip_code>')
def current_weather(zip_code):
  if weather.valid_zip_code(zip_code):
    response = build_response('success', weather.get_current(zip_code), 200)
  else:
    response = build_response('failure', 'bad request', 400)

  return response

# get forecast for zip code
@app.route('/weather/forecast/<zip_code>')
def forecast(zip_code):
  if weather.valid_zip_code(zip_code):
    response = build_response('success', weather.get_forecast(zip_code), 200)
  else:
    response = build_response('failure', 'bad request', 400)

  return response

def build_response(message, data, status):
  response = {'message': message, 'data': data}
  return jsonify(response), status


