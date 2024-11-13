import json
def transToAxis(loc):
    citycode = None
    with open('axisCode.json') as f:
        citycode = json.load(f)

    return citycode["city"][loc["city"]][loc["district"]]

    
