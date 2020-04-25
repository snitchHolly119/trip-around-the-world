from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import environ
import wikipedia
from random import randint


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
    new_destination=randint(1, 40)
    return render_template("index.html", destination=new_destination)


@app.route("/<int:location_id>")
def location_page(location_id):
    bg_color =f"{randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)}"
    current_location = Locations.query.get(location_id)
    return render_template("location_page.html", location = current_location, bg_color=bg_color)
