from datetime import datetime
import requests,pytz

def getAirData(lon,lat): 
    nowTime = datetime.now(pytz.timezone('Asia/Taipei')).strftime("%Y-%m-%d %H:%M:%S")#取得符合取得資料格式的時間
    url = f"https://data.moenv.gov.tw/api/v2/aqx_p_432?&api_key=7fcc7250-55c6-497a-aa44-cfba6d8f2c83&filters=publishtime,LE,{nowTime}&fields=sitename,aqi,pm2.5,longitude,latitude"
    try:
        AQIData = requests.get(url, verify=False).json()["records"]# 把憑證改回來
        distant = float(100)
        siteName = None
        for site in AQIData:
            distant_temp = (((float(site["longitude"])-lon)**2)+(((float(site["latitude"])-lat)**2)))**0.5
            if distant_temp < distant :
                distant = distant_temp
                siteName = site
        if(siteName):
            return {
                "sitename": siteName["sitename"],
                "aqi":      siteName["aqi"],
                "pm2.5":    siteName["pm2.5"]
            }
        else:
            return {
                "sitename": None,
                "aqi":      None,
                "pm2.5":    None,
                "error":    "siteName no data",
                "dis":      distant,
                "time":     nowTime
            }
    except Exception as e :
            return {
                "sitename": None,
                "aqi":      None,
                "pm2.5":    None,
                "error":    e,
                "dis":      distant,
                "time":     nowTime
            }
    
