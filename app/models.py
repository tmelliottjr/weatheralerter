from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  phone = db.Column(db.String)
  zip_code = db.Column(db.String)
  subscribed = db.Column(db.Boolean)

  def __repr__(self):
    return f'<User {self.id}>'


