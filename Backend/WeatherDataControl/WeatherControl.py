from flask import Blueprint,request,jsonify,make_response
import dataHandler.weatherData
import json
import sqlite3
from flask_cors import CORS
weatherControl_blueprint = Blueprint('weatherControl_blueprint', __name__)
CORS(weatherControl_blueprint)
DATABASE = 'data.sqlite'
conn = sqlite3.connect(DATABASE,check_same_thread=False)
cursor = conn.cursor()
@weatherControl_blueprint.route('/Get12hData',methods=['POST'])
def Get12hData():
    data = request.get_json()
    userID = data.get('userID')
    pre_cusloc = data.get('cusloc')
    if pre_cusloc == None:
        result = {
            "Stats" : "Index Error. Please Follow Documentaion Instructions"
            }
        response = make_response(jsonify(result),404)
        return response
    a = dataHandler.weatherData.get12hData(pre_cusloc)
    if userID != None:
        counter = len(cursor.execute("Select * from users where id=?",[userID]).fetchall())
        if counter > 0:
            cursor.execute("UPDATE users set city =? where id =?",(a[0]["city"],userID))
            print("Save Region Successfully")
            conn.commit()
    return jsonify(a)
@weatherControl_blueprint.route('/Get3hData',methods=['POST'])
def Get3hData():
    data = request.get_json()
    userID = data.get('userID')
    pre_cusloc = data.get('cusloc')
    if pre_cusloc == None:
        result = {
            "Stats" : "Index Error. Please Follow Documentaion Instructions"
            }
        response = make_response(jsonify(result),404)
        return response
    a = dataHandler.weatherData.get3hData(pre_cusloc)
    if userID != None:
        counter = len(cursor.execute("Select * from users where id=?",[userID]).fetchall())
        if counter > 0:
            cursor.execute("UPDATE users set city =? where id =?",(a[0]["city"],userID))
            print("Save Region Successfully")
            conn.commit()
    return jsonify(a)
