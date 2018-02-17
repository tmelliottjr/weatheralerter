from flask import render_template, request, jsonify
from app import app, db
from app.apis import sms, weather
from app.models import User

# FIXME: better validation and failure response

# subscribe to service
@app.route('/subscribe', methods=['POST'])
def subscribe():
  req = request.get_json(force=True)
  phone_number = req['phone_number']
  zip_code = req['zip_code']
  user = User.query.filter(User.phone_number == phone_number).first()
  
  if not user:
    user = User()
    user.phone_number = phone_number

  user.verification_code = User.generate_verification_code()
  user.zip_code = zip_code

  db.session.add(user)
  db.session.commit()

  #FIXME better error handling on failed message send
  user.send_verification_code()

  return build_response('success', f'Verification text message sent to {user.phone_number}.', 200)

@app.route('/verify', methods=['POST'])
def verify_subscription():
  req = request.get_json(force=True)
  phone_number = req['phone_number']
  verification_code = req['verification_code']

  user = User.query.filter(User.phone_number == phone_number).first()

  # FIXME: move to user controller
  if user:
    if user.verify_verification_code(verification_code):
      user.subscribed = True
      user.verification_code = ''
      sms.send(user.phone_number, 'Your WeatherAlerter subscription has been confirmed!')
      response = build_response('success', 'account verified', 200)
    else:
      response = build_response('failure', 'invalid verification code', 400)
  else:
    response = build_response('failure', 'account not found', 404)

  db.session.add(user)
  db.session.commit()

  return response


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

# TODO: Move to sms helpers 
@app.route('/sms/', methods=['POST'])
def sms_handler():
  if request.form['Body'].upper() == 'HELPME':
    print('we should create a response object and return!') 
  else:
    print(request.form)
  return 'success'  

def build_response(message, data, status):
  response = {'message': message, 'data': data}
  return jsonify(response), status


