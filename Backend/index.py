from flask import Flask,jsonify
from flask_restful import Resource, Api
from flask import g
import os
import sqlite3
DATABASE = 'Backend/data.sqlite'
app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return 'hello there'
@app.route('/getAllWeatherData')
def getAllWeatherData():
    return None

if __name__ == '__main__':
    app.debug = True
    app.run()