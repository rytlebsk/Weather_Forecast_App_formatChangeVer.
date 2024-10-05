from flask import Blueprint,request,jsonify,make_response
import dataHandler.weatherData
weatherControl_blueprint = Blueprint('weatherControl_blueprint', __name__)

@weatherControl_blueprint.route('/Get12hData',methods=['POST'])
def Get12hData():
    '''
    {
    "longitude" : "xxxx",
    "latitude" : "xxxx",
    }
    '''
    data = request.get_json()
    pre_longtitud = data.get('longitude')
    pre_latitude = data.get('latitude')
    if pre_longtitud == None or pre_latitude == None:
        result = {
            "Stats" : "Index Error. Please Follow Documentaion Instructions"
            }
        response = make_response(jsonify(result),404)
        return response
    longtitude = float(pre_longtitud)
    latitude = float(pre_latitude)
    a = dataHandler.weatherData.get12hData(longtitude,latitude)
    return jsonify(a)
@weatherControl_blueprint.route('/Get3hData',methods=['POST'])
def Get3hData():
    '''
    {
    "longitude" : "xxxx",
    "latitude" : "xxxx",
    }
    '''
    data = request.get_json()
    pre_longtitud = data.get('longitude')
    pre_latitude = data.get('latitude')
    if pre_longtitud == None or pre_latitude == None:
        result = {
            "Stats" : "Index Error. Please Follow Documentaion Instructions"
            }
        response = make_response(jsonify(result),404)
        return response
    longtitude = float(data.get('longitude'))
    latitude = float(data.get('latitude'))
    a = dataHandler.weatherData.get3hData(longtitude,latitude)
    return jsonify(a)
