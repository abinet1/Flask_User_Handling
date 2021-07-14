from flask_login.mixins import UserMixin
from Flask_User_Handling import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(10),unique=True, nullable=False)
	email = db.Column(db.String(120),unique=True, nullable=False)
	profile_image = db.Column(db.String(20), nullable=False, default='default.jpg')
	password =  db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.profile_image}')"
