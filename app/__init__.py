#!/usr/bin/python3
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config) #app.config['SECRET_KEY'] = 'you-will-never-guess'
#print(dir(Config))

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes above to create app object
from app import routes, models

