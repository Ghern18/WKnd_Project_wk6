from datetime import datetime

from app import db

class PowerModel(db.Model):

  __tablename__ = 'powers'

  id = db.Column(db.Integer, primary_key = True)
  body = db.Column(db.String, nullable = False)
  timestamp = db.Column(db.String)
  xmen_id = db.Column(db.Integer, db.ForeignKey('xmen.id'), nullable = False)

  def __repr__(self):
    return f'<Power: {self.body}>'
  
  def commit(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()