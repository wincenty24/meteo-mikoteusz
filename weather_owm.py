from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import json


"""
owm = OWM('349af6d6cf9a308d229cf059fc3c81d6')
mgr = owm.weather_manager()


reg = owm.city_id_registry()
loc = reg.locations_for('Warsaw', country='PL')
one_call = mgr.one_call(loc[0].lat, loc[0].lon)
forecast = one_call.forecast_daily
"""
#json_file = json.dumps(userdata_dict)

class forecast_weather():
    def __init__(self, lat, lon):
        self._key = "349af6d6cf9a308d229cf059fc3c81d6"

        self.owm = OWM(self._key)
        mgr = self.owm.weather_manager()
        self.one_call = mgr.one_call(lat, lon)

    def next_week(self):
        userdata_dict = {"data0": [], "data1": [], "data2": [], "data3": [], "data4": [], "data4": [], "data5": [],
                         "data6": [], "data7": []}

        forecast = self.one_call.forecast_daily
        for x in range(0, len(forecast)):
            userdata = {}
            reference_time = forecast[x].reference_time
            sunset_time = forecast[x].sunset_time
            sunrise_time = forecast[x].sunrise_time
            clouds = forecast[x].clouds
            rain = forecast[x].rain
            snow = forecast[x].snow
            wind = forecast[x].wind
            humidity = forecast[x].humidity
            pressure = forecast[x].pressure
            temperature = forecast[x].temperature('celsius')
            status = forecast[x].status
            detailed_status = forecast[x].detailed_status
            weather_code = forecast[x].weather_code
            weather_icon_name = forecast[x].weather_icon_name
            visibility_distance = forecast[x].visibility_distance
            dewpoint = forecast[x].dewpoint
            humidex = forecast[x].humidex
            heat_index = forecast[x].heat_index
            utc_offset = forecast[x].utc_offset
            uvi = forecast[x].uvi

            userdata['reference_time'] = str(reference_time("date"))
            userdata['sunset_time'] = str(sunset_time("date"))
            userdata['sunrise_time'] = str(sunrise_time("date"))
            userdata['clouds'] = clouds
            userdata['rain'] = rain
            userdata['snow'] = snow
            userdata['wind'] = wind("km_hour")
            userdata['humidity'] = humidity
            userdata['pressure'] = pressure
            userdata['temperature'] = temperature
            userdata['status'] = status
            userdata['detailed_status'] = detailed_status
            userdata['weather_code'] = weather_code
            userdata['weather_icon_name'] = weather_icon_name
            userdata['visibility_distance'] = visibility_distance
            userdata['dewpoint'] = dewpoint
            userdata['humidex'] = humidex
            userdata['heat_index'] = heat_index
            userdata['utc_offset'] = utc_offset
            userdata['uvi'] = uvi

            userdata_dict[f"data{x}"].append(userdata)

        return userdata_dict






