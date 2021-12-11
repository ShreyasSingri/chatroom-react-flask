from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:2021@localhost/ChatApp"
db = SQLAlchemy(app)


class RegisteredUsers(db.Model):
    name = db.Column(db.String(100), primary_key = True, unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), unique = False, nullable=False)
