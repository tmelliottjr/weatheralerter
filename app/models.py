import random
from app import db
from app.apis import sms

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  phone_number = db.Column(db.String(10))
  zip_code = db.Column(db.String(5))
  subscribed = db.Column(db.Boolean)
  verification_code = db.Column(db.String(6))

  def __repr__(self):
    return f'<User {self.id}>'
  
  @classmethod
  def generate_verification_code(User):
    return random.randrange(100000, 999999)
    
  def verify_verification_code(self, data):
    return self.verification_code == data

  def send_verification_code(self):
    body = f'Your subscription verification code is: {self.verification_code}'
    sms.send(self.phone_number, body)
    return
