from firebase import firebase
import tkinter as tk



class forecast_taker:
    def __init__(self):
        self.firebase = firebase.FirebaseApplication("https://meteo-mikoteusz-default-rtdb.firebaseio.com/", None)
        self.temp = self.firebase.get(f"Weather_requirements/results/user_1/", '')
        self.clouds=[]
        self.detailed_status = []
        self.point = []
        self.humidity = []
        self.pressure = []
        self.rain = []
        self.ref_time = []
        self.sunrise_time = []
        self.sunset_time = []
        self.tem_day = []
        self.tem_eve = []
        self.tem_feels_like_day = []
        self.tem_feels_like_eve = []
        self.tem_feels_like_morn = []
        self.tem_feels_like_night = []
        self.tem_max = []
        self.tem_min = []
        self.tem_morn = []
        self.tem_night = []
        self.wind_deg = []
        self.wind_gust = []
        self.wind_speed = []
        self.status=[]

    def take_it(self):
        if str(self.temp)!=None:
            for x in self.temp:
                self.how_many_days = len(self.temp[x])
                cout = 0
                for y in self.temp[x]:
                    print(y)
                    if y != "result":
                        for z in y:
                            for c in z:
                               if c == "clouds":
                                    self.clouds.append( str(z['clouds']))
                               else:
                                   self.clouds.append(str(0))


                            self.detailed_status.append(z['detailed_status'])
                            self.point .append( str(z['dewpoint']))
                            self.humidity.append( str(z['humidity']))
                            _pres= z['pressure']
                            self.pressure.append(str(_pres['press']))

                            if c == "rain":
                                _rain = z['rain']
                                self.rain.append(str(_rain['all']))
                            else:
                                self.rain.append(str(0))


                            self.ref_time.append( str(z['reference_time']))
                            self.status.append(str(z['status']))
                            self.sunrise_time.append(str(z['sunrise_time']))
                            self.sunset_time.append(str(z['sunset_time']))
                            _tem=z['temperature']
                            #print(_tem['day'])
                            #self.tem_day=str(_tem['day'])
                            self.tem_day.append(str( _tem['day']))
                            self.tem_eve.append( str(_tem['eve']))
                            self.tem_feels_like_day.append( str(_tem['feels_like_day']))
                            self.tem_feels_like_eve.append(str(_tem['feels_like_eve']))
                            self.tem_feels_like_morn.append( str(_tem['feels_like_morn']))
                            self.tem_feels_like_night.append( str(_tem['feels_like_night']))
                            self.tem_max.append( str(_tem['max']))
                            self.tem_min.append(str(_tem['min']))
                            self.tem_morn.append(str(_tem['morn']))
                            self.tem_night.append(str(_tem['night']))
                            _wind=z['wind']
                            self.wind_deg.append(str(_wind['deg']))
                            self.wind_gust.append(str(_wind['gust']))
                            self.wind_speed.append(str(_wind['speed']))




print(forecast_taker().take_it())