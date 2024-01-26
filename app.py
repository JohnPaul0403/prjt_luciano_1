import os
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from app_blueprint import app_blueprint, cover_blueprint

load_dotenv()

# Database interaction
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# Table for database
class User(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(40), nullable=False)
    lname = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(40), unique=True, nullable=False)

# Create self variable
def __init__(self, fname, lname, password):
    self.fname = fname
    self.lname = lname
    self.password = password

app.register_blueprint(app_blueprint)
app.register_blueprint(cover_blueprint)

#get web url access
@app.route('/')
def index():
    return render_template('index.html')

#API...
@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        password = request.form['password']

        user = User(fname, lname, password)
        db.session.add(database_agar)
        db.session.commit()
 
