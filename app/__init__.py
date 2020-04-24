from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import environ


app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['FLASK_DEBUG'] = environ.get('FLASK_DEBUG')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db =SQLAlchemy(app)
migrate = Migrate(app, db)



from app import app
from app.models import Locations

@app.route("/")
def index():
    location_list = Locations.query.all()
    return render_template("index.html", locations=location_list)
