from flask import Blueprint,request,jsonify,make_response
import dataHandler.weatherData
import json
from flask_cors import CORS
weatherControl_blueprint = Blueprint('weatherControl_blueprint', __name__)
CORS(weatherControl_blueprint)
@weatherControl_blueprint.route('/Get12hData',methods=['POST'])
def Get12hData():
    data = request.get_json()
    pre_longtitud = data.get('longitude')
    pre_latitude = data.get('latitude')
    pre_cusloc = data.get('cusloc') if data.get('cusloc') != None else ""
    if pre_longtitud == None or pre_latitude == None:
        result = {
            "Stats" : "Index Error. Please Follow Documentaion Instructions"
            }
        response = make_response(jsonify(result),404)
        return response
    longtitude = float(pre_longtitud)
    latitude = float(pre_latitude)
    a = dataHandler.weatherData.get12hData(longtitude,latitude,pre_cusloc)
    return jsonify(a)
@weatherControl_blueprint.route('/Get3hData',methods=['POST'])
def Get3hData():
    data = request.get_json()
    pre_longtitud = data.get('longitude')
    pre_latitude = data.get('latitude')
    pre_cusloc = data.get('cusloc') if data.get('cusloc') != None else ""
    if pre_longtitud == None or pre_latitude == None:
        result = {
            "Stats" : "Index Error. Please Follow Documentaion Instructions"
            }
        response = make_response(jsonify(result),404)
        return response
    longtitude = float(data.get('longitude'))
    latitude = float(data.get('latitude'))
    a = dataHandler.weatherData.get3hData(longtitude,latitude,pre_cusloc)
    return jsonify(a)
