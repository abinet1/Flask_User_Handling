from flask import Flask,render_template,url_for,flash, redirect
from flask_sqlalchemy import SQLAlchemy
from Form import RegistretionForm,LoginForm

app=Flask(__name__)

app.config['SECRET_KEY'] = '275a2480f58a41dc98bd4f302335af51'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(10),unique=True, nullable=False)
	email = db.Column(db.String(120),unique=True, nullable=False)
	profile_image = db.Column(db.String(20), nullable=False, default='default.jpg')
	password =  db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.profile_image}')"

@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		if form.email.data=='admin@gmail.com' and form.password.data=='pass1.':
			flash(f'you have success loged in.','success')
			return redirect(url_for('index'))
	return render_template('login.html',form=form)

@app.route('/signup', methods=['GET','POST'])
def signup():
	form=RegistretionForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('index'))
	return render_template('signup.html', form=form)

