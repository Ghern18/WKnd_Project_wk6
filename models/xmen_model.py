from datetime import datetime

from app import db

from werkzeug.security import generate_password_hash, check_password_hash

followers = db.Table( 'followers',
  db.Column('follower_id', db.Integer, db.ForeignKey('xmen.id')),
  db.Column('followed_id', db.Integer, db.ForeignKey('xmen.id'))  
)

class XmenModel(db.Model):

    __tablename__ = 'xmen'

    xmen_id = db.Column(db.Integer, primary_key = True)
    xmen = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String(75), nullable = False, unique = True)
    password_hash = db.Column(db.String(250), nullable = False)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    followed = db.relationship('StudentModel',
                            secondary = 'followers',
                            primaryjoin = followers.c.follower_id == id,
                            secondaryjoin = followers.c.followed_id == id,
                            backref = db.backref('followers', lazy = 'dynamic')
                            )
    powers = db.relationship('PowerModel',back_populates ='xmen', lazy='dynamic', cascade= 'all, delete')

    def __repr(self):
        return f'<Xmen: {self.student}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, student_dict):
        for k, v in student_dict.items():
            if k != 'password':
                setattr(self, k, v)
            else:
                setattr(self, 'password_hash', generate_password_hash(v))
        # self.password_hash = v

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_following(self, student):
        return student in self.followed
  
    def follow(self, student):
        if self.is_following(student):
           return
        self.followed.append(student)

    def unfollow(self,student):
       if not self.is_following(student):
          return
       self.followed.remove(student)

class PowerModel(db.Model):

  __tablename__ = 'spells'

  id = db.Column(db.Integer, primary_key = True)
  body = db.Column(db.String, nullable = False)
  timestamp = db.Column(db.DateTime, default = datetime.utcnow)
  student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable = False)
  student = db.relationship('UserModel', back_populates = 'powers')

  def __repr__(self):
    return f'<Power: {self.body}>'
  
  def commit(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()