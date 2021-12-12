Introduction
This is a chat application, implemented using Flask-SocketIO with the database (PostgreSQL).

commands for running the code:--
virtualenv venv
. ./venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=run.py
flask run

Demonstration of a Flask application with live chat functionality. Comments are added to the page for all connected clients, and the page views automatically updates as well.

Live chat: Using Javascript, SocketIO, and Python. All messages are sent to the Python web server, and then broadcast back to all clients.
Persistent chat: Utilizing flask-sqlalchemy, all chat messages are saved and are added to the page for any other people joining the chat page.

Files in the program
run.py: This is the main app file and contains both the registration/login page logic and the Flask-SocketIO backend for the app.
connection.py: Contains Flask-SQLAlchemy models used for user registration and login in application.py
requirements.txt: list of Python packages installed 
templates/: folder with all HTML files
static/: for with all JS scripts and CSS files