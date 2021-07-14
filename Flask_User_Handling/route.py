from wtforms.validators import Email
from Flask_User_Handling import bcrypt
from Flask_User_Handling.models import User
from Flask_User_Handling import app, oauth
from flask_login import login_required, login_user, logout_user, current_user
from flask import render_template, redirect, flash, url_for, session
from Flask_User_Handling.form import RegistretionForm,LoginForm


@app.route('/home')
@login_required
def index():
	return render_template('index.html', user=current_user)

@app.route('/login', methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user)
			return redirect(url_for('index'))
	return render_template('login.html',form=form)

@app.route('/signup', methods=['GET','POST'])
def signup():
	form=RegistretionForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('index'))
	return render_template('signup.html', form=form)


@app.route('/g-login')
def g_login():
	google= oauth.create_client('google')
	redirect_uri = url_for('g_auth', _external=True)
	return google.authorize_redirect(redirect_uri)

@app.route('/g-auth')
def g_auth():
	google =oauth.create_client('google')
	token = google.authorize_access_token()
	user = google.parse_id_token(token)	
	c_user=User.query.filter_by(email=user.email).first()
	login_user(c_user)
	return redirect(url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return "you are logged out"