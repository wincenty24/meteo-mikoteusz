from weather_taker import weather
from data_pusher import  pusher
from  data_taker import data_fb_taker
from weather_owm import forecast_weather
import json
from forecast import Forecast
import time
from pyowm import OWM

owm = OWM('349af6d6cf9a308d229cf059fc3c81d6')
mgr = owm.weather_manager()

reg = owm.city_id_registry()

while(True):
    Forecast().fun()
    time.sleep(1)


   #print(data_in_place['reference_time'])

#pusher().push_with_random_package(f"Weather_requirements/results/user_1/",)
#print( str({'-M_beYUOMwpwXvU9YAUF': {'Warsaw': {'clouds': {'type': 'hight', 'val': 9}, 'detailed_status': 'clear sky', 'humidity': {'type': 'hight', 'val': 46}, 'pressure': {'press': {'type': 'hight', 'val': 1014}, 'sea_level': 'None'}, 'reference_time': ['2021-05-13 10:00:00+00:00', '2021-05-14 10:00:00+00:00'], 'status': 'Clear', 'sunrise_time': '2021-05-11 02:47:24+00:00', 'sunset_time': '2021-05-11 18:17:20+00:00', 'temperature': {'day': {'type': 'hight', 'val': 22.61}, 'eve': {'type': 'hight', 'val': 23.19}, 'feels_like_day': {'type': 'hight', 'val': 22.13}, 'feels_like_eve': {'type': 'hight', 'val': 22.58}, 'feels_like_morn': {'type': 'hight', 'val': 12.58}, 'feels_like_night': {'type': 'hight', 'val': 12.58}, 'max': {'type': 'hight', 'val': 23.86}, 'min': {'type': 'hight', 'val': 7.95}, 'morn': {'type': 'hight', 'val': 13.12}, 'night': {'type': 'hight', 'val': 17.18}}, 'wind': {'deg': {'type': 'hight', 'val': 140}, 'gust': {'type': 'hight', 'val': 53.82}, 'speed': {'type': 'hight', 'val': 26.856}}}}}
#).replace("'",'"'))



    #print(x ,loc)
    ##file=json.dumps(q)
    #print(q)



"""
pusher().push_without_random_package("Search_place","user_1/Place", "Opole")
place = data_fb_taker().get_saved_place("user_1")   
weather_for = weather(place).curren()
pusher().push_with_random_package(f"Saved_place/user_1/{place}/",weather_for)
"""
