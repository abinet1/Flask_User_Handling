from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Length,DataRequired,Email,EqualTo
import email_validator

class RegistretionForm(FlaskForm):
	username = StringField('Username',validators=[Length(min=2,max=10),DataRequired()])
	email = StringField('Email', validators=[Email(),DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[Email(),DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Login')