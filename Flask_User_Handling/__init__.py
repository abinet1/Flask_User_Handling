from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from authlib.integrations.flask_client import OAuth
from flask_login import LoginManager

app=Flask(__name__)

app.config['SECRET_KEY'] = '275a2480f58a41dc98bd4f302335af51'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = SQLAlchemy(app)
oauth = OAuth(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
bcrypt = Bcrypt(app)

oauth.register(
    'google',
    client_id='your own google client id.....',
    client_secret='your own google client secret key....',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'}
)

from Flask_User_Handling import route