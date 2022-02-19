#!/usr/bin/python3
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config) #app.config['SECRET_KEY'] = 'you-will-never-guess'
#print(dir(Config))
# Import routes above to create app object
from app import routes

# if __name__ == '__main__':
#     app.run(debug=True)
