from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:pass@localhost/chatapp"
db = SQLAlchemy(app)


class RegisteredUsers(db.Model):
    # __tablename__='registered_users'
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), unique = False, nullable=False)
