class UserDataResult():
    def __init__(self,id,account,password,status):
        self.id = id
        self.account = account
        self.password = password
        self.status = status
    def to_dict(self):
        return {
            "id": self.id,
            "account" : self.account,
            "password": self.password,
            "status": self.status
        }
class Habit():
    def __init__(self,id,habitName):
        self.id = id
        self.habitName = habitName
    def to_dict(self):
        return {
            "id": self.id,
            "habitName" : self.habitName
        }
class Sport():
    def __init__(self,id,sportName):
        self.id = id
        self.sportName = sportName
    def to_dict(self):
        return {
            "id": self.id,
            "sportName" : self.sportName
        }
class SportsSuggestion():
    def __init__ (self,sportName,sportSuggestion):
        self.name = sportName
        self.suggestion = sportSuggestion
    def to_dict(self):
        return {
                "name": self.name,
                "suggestion" : self.suggestion
            }
    
class HabitsSuggestion():
    def __init__(self,habitName,habitSuggestion):
        self.name = habitName
        self.suggestion = habitSuggestion
    def to_dict(self):
        return {
                "name": self.name,
                "suggestion" : self.suggestion
                }
    
class DailySuggestion():
    def __init__(self,nowWeatherData):
        self.nowWeatherData = nowWeatherData
    def getSportsSuggestion(self):
        nowRainRate = self.nowWeatherData["rainRate"]
        nowPM = self.nowWeatherData["pm2.5"]
        nowAirQuality = self.nowWeatherData["aqi"]
        nowTemp = self.nowWeatherData["temp"]
        basketballSuggetstion = ""
        badmintonSuggestion = ""
        volleyballSuggestion = ""
        tabletennisSuggestion = ""
        runSuggestion = ""
        swimSuggestion = ""
        bikeSuggestion = ""
        result = []
        if int(nowRainRate) > 50:
            basketballSuggetstion = "今天可能下雨，不適合打籃球！"
            badmintonSuggestion = "今天可能下雨，不要在戶外打羽毛球！"
            volleyballSuggestion = "今天可能下雨，不要在戶外打排球！"
            tabletennisSuggestion = "今天適合打乒乓球！"
            
        else:
            basketballSuggetstion = "今天適合打籃球！"
            badmintonSuggestion = "今天無論室外或室內都適合打羽毛球！"
            volleyballSuggestion = "今天適合打排球，不論室外或室內！"
            tabletennisSuggestion = "今天適合打乒乓球！"
        if nowAirQuality != None and nowAirQuality != "fetch data error" and int(nowAirQuality) > 100:
            runSuggestion = "今天空氣品質好，適合跑步或慢跑！"
            bikeSuggestion = "今天空氣品質好，適合騎自行車！"
        else:
            runSuggestion = "由於空氣品質不好，今天跑步或慢跑可能不是一個好的選擇！"
            bikeSuggestion = "由於空氣品質不好，今天跑步或慢跑可能不是一個好的選擇！"
        if int(nowTemp) > 25:
            swimSuggestion = "如果您今天打算游泳，別忘了多喝水！"
        else:
            swimSuggestion = "如果您今天打算游泳，請照顧好自己的身體！"
        result.append(basketballSuggetstion)
        result.append(badmintonSuggestion)
        result.append(volleyballSuggestion)
        result.append(swimSuggestion)
        result.append(bikeSuggestion)
        result.append(runSuggestion)
        result.append(tabletennisSuggestion)
        return result
    
    def getHabitsSuggestion(self):
        nowRainRate = self.nowWeatherData["rainRate"]
        nowAirQuality = self.nowWeatherData["aqi"]
        nowTemp = self.nowWeatherData["temp"]
        dessertSuggestion = ""
        hikingSuggestion = ""
        mountainSuggestion = ""
        gameSuggestion = ""
        outdoorSuggestion = ""
        studySuggestion = "不管現在天氣如何，你都可以去閱讀"
        result = []
        if int(nowRainRate) > 50 :
            dessertSuggestion = "今天可能下雨，在室內做甜點是不錯的選擇！"
            gameSuggestion ="今天可能下雨，在室內做甜點是不錯的選擇！"
            hikingSuggestion ="今天可能會下雨，今天徒步旅行不是一個好的選擇！"
            mountainSuggestion ="今天可能會下雨，今天爬山不是一個好的選擇！"
            outdoorSuggestion ="今天可能會下雨，別忘了帶傘！"
        else:
            dessertSuggestion ="今天天氣不錯，不過做甜點還是不錯的選擇！"
            gameSuggestion ="今天天氣不錯，不過玩遊戲還是不錯的選擇！"
            hikingSuggestion = "今天天氣很好，適合去健行！"
            mountainSuggestion = "今天天氣很好，適合去爬山！"
            outdoorSuggestion = "今天天氣很好，適合戶外活動！"
            if int(nowTemp) > 30:
                hikingSuggestion = "今天很熱，如果要去健行，別忘了多喝水！"
                mountainSuggestion = "今天很熱，如果要去爬山，別忘了多喝水！"
                outdoorSuggestion = "今天很熱，如果有戶外活動，別忘了多喝水！"
            if nowAirQuality is not None and nowAirQuality != "fetch data error" and int(nowAirQuality) > 100:
                hikingSuggestion = "今天空氣品質不好，建議不要去健行"
                mountainSuggestion = "今天空氣品質不好，建議不要去爬山"
                outdoorSuggestion = "今天空氣品質不好，若有戶外活動，記得戴口罩"
            result.append(dessertSuggestion)
            result.append(hikingSuggestion)
            result.append(mountainSuggestion)
            result.append(gameSuggestion)
            result.append(outdoorSuggestion)
            result.append(studySuggestion)
            return result

    def getDressingSuggestion(self):
        nowRainRate = self.nowWeatherData["rainRate"]
        nowTemp = self.nowWeatherData["temp"]
        result = ""
        if int(nowTemp) > 30:
            result += "今天很熱，可以穿少一點衣服。"
        elif 20 < int(nowTemp) <= 30:
            result += "今天天氣涼爽，別忘了帶件外套。"
        else:
            result += "今天非常冷，盡量不要出門，記得穿上外套。"
        if int(nowRainRate) >= 60:
            result += "而且別忘了帶雨傘！"
        return result

    def getHealthSuggestion(self):
        nowPM = self.nowWeatherData["pm2.5"]
        nowBodyTemp = self.nowWeatherData["bodyTemp"]
        result = ""
        if nowPM is not None and nowPM != "fetch data error" and int(nowPM) > 15:
            result += "今天空氣不好，記得戴口罩。"
        else:
            result += "今天空氣品質良好。"
        if nowBodyTemp is not None and int(nowBodyTemp) > 30:
            result += "別忘了多喝水，因為天氣炎熱！"
        else:
            result += "記得多喝水，對身體有益！"
        return result

    def getTransportationSuggestion(self):
        nowRainRate = self.nowWeatherData["rainRate"]
        result = ""
        if int(nowRainRate) > 50:
            result += "今天可能會下雨，建議開車或搭乘大眾交通工具。"
        else:
            result += "今天降雨機率不高，可以騎自行車或步行通勤。"
        return result



