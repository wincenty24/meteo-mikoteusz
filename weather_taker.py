import json
import requests
from datetime import datetime

class weather:
    _api_key = "349af6d6cf9a308d229cf059fc3c81d6"
    def __init__(self, city_name):
        self.city_name = city_name

    def curren(self):

        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + self._api_key + "&q=" + self.city_name
        response = requests.get(complete_url)
        dictionary = response.json()
        dictionary["time:"] = self._take_current_time()
        json_file = json.dumps(dictionary)
        return dictionary

    def forecast(self, lat, lon):
        url = f"https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=daily&appid={self._api_key}&units=metric"

        response = requests.get(url)
        dictionary = response.json()
        dictionary.pop("current")
        dictionary.pop("minutely")
        json_file = json.dumps(dictionary)

        return dictionary

    def _take_current_time(self):
        return str(datetime.today().strftime("%d/%m/%Y %H:%M:%S"))

    def _kelvin_to_cel(self, kelvin):
        return kelvin - 273.15
"""

https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=349af6d6cf9a308d229cf059fc3c81d6

"""