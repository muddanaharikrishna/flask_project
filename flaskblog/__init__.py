from flask import Flask, render_template, url_for, flash, redirect
# before connect the database install sqlalchemy - pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# import secrets from python shell  ex: >>> import secrets
# enter secrets.token_hex(16) for 16 char/num key
app.config['SECRET_KEY'] = '94e035d327e362ea8d7d6a31188d1c97'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# routes are to be connected db after calling only, this cause mentioned after db=SQLAlchemy(app)
from flaskblog import routes
