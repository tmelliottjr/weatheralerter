from flask import render_template, request, jsonify
from app import app

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
  return jsonify({'message': 'success'})

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
  return jsonify({'message':'success'})
  