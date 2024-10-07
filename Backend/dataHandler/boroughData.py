import json
def GetBoroughCode():
    citycode = None
    with open('boroughCode.json') as f:
        citycode = json.load(f)
    return citycode