# Introduction
This is a chat application, implemented using Flask-SocketIO with the database (PostgreSQL).

Demonstration of a Flask application with live chat functionality. Comments are added to the page for all connected clients, and the page views automatically updates as well.

Live chat: Using Javascript, SocketIO, and Python. All messages are sent to the Python web server, and then broadcast back to all clients.
Persistent chat: Utilizing flask-sqlalchemy, all chat messages are saved and are added to the page for any other people joining the chat page.

Frontend is build using React.
Backend is build using Flask.

## Commands for running the code
1) git clone https://github.com/ShreyasSingri/chatroom-react-flask
2) virtualenv venv <br>
. ./venv/bin/activate <br>
pip install -r requirements.txt <br>
export FLASK_APP=run.py <br>
flask run <br>

3) create a database chatapp <br>

## Files in the program
run.py: This is the main app file and contains both the registration/login page logic and the Flask-SocketIO backend for the app.<br>
connection.py: Contains Flask-SQLAlchemy models used for user registration and login in application.py <br>
requirements.txt: list of Python packages installed  <br>
templates/: folder with all HTML files <br>
static/: for with all JS scripts and CSS files <br>

### Database
We have created a postgres database "chatapp" for registering the users using chatapp and then fetching the users while logging in.
Chatapp database has a table "registered_users" which is automatically created when we run the connection.py file and has the following parameters.<br>
id,name,email and password. <br>
All these parameters are taken from the user while registration.<br>
For logging in user has to enter its email and password.<br>


### API
We have created api for login and register.<br>

API FOR LOGIN AND REGISTER:-

Register API <br>
API endpoint will check that is http request method is get, than render registration form but if the http request method is post, than it will check that form is valid or not, if form is valid, it will create new user object with that password and then it will save that object inside the Database.<br>
Login API <br>
Here, if the method is post and the form is valid, then it will search the user in the Database using the user's email. if user exist than it will compare the hashed password which is stored inside the database and simple password which is entered by user
