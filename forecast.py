from weather_taker import weather
from data_pusher import  pusher
from  data_taker import data_fb_taker
from weather_owm import forecast_weather
import json


class Forecast():
  _weather_data= None
#usówanie reque

  def fun(self):
    items = 0
    taken_places=data_fb_taker().get_weather_req()
    print(taken_places)
    if taken_places!= None:
      _weather_dic = []
      _weather_bool = None
      add_to_dic=[]
      for places_data in taken_places:

          coord = taken_places[places_data]
          for place in coord:

              place1=place.replace("-",".").replace("?"," ").split(" ")
              place_detalis = coord[place]
              _weather_data = forecast_weather(float(place1[0]), float(place1[1])).next_week()
              for data_inside_weather_data in _weather_data:
                  is_taken = True
                  detalis_weather_data = _weather_data[data_inside_weather_data]
                  #detalis_weather_data_time = detalis_weather_data["reference_time"]
                  for data_weather in detalis_weather_data:

                      detalis_weather_data_time=data_weather["reference_time"]
                      #how_many_ref_times=len(detalis_weather_data)

                      for place_detalis_time in place_detalis["reference_time"]:
                        if detalis_weather_data_time == place_detalis_time:
                            for x in place_detalis:
                                for y in data_weather:
                                  if (x == y):
                                    bul = True
                                    if x =="temperature":
                                      f=place_detalis[x]
                                      g=data_weather[y]
                                      _days_arr = {"day", "eve", "feels_like_day", "feels_like_eve", "feels_like_morn",
                                                   "feels_like_night", "max", "min", "morn", "night"}

                                      for temp_detlis in _days_arr:
                                        #if g[temp_detlis] == f[temp_detlis]:
                                        j=f[temp_detlis]

                                        if(j["type"]=="high"):
                                          if float(g[temp_detlis]) > float(j["val"]):
                                            pass
                                          else:
                                            bul = False
                                        elif (j["type"] == "low"):
                                          if float(g[temp_detlis]) < float(j["val"]):
                                            pass
                                          else:
                                            bul = False
                                        elif (j["type"] == "EQ"):
                                          if float(g[temp_detlis]) != float(j["val"]):
                                            bul = False

                                    elif x == "wind":
                                      f = place_detalis[x]
                                      g = data_weather[y]
                                      _days_arr = {"deg", "gust", "speed"}
                                      for wind_detlis in _days_arr:
                                        # if g[temp_detlis] == f[temp_detlis]:
                                        j = f[wind_detlis]

                                        if (j["type"] == "high"):
                                          if float(g[wind_detlis]) > float(j["val"]):
                                            # return True
                                            pass
                                          else:
                                            bul = False
                                        elif (j["type"] == "low"):
                                          if float(g[wind_detlis]) < float(j["val"]):
                                            pass
                                          else:
                                            bul = False
                                        elif (j["type"] == "EQ"):
                                          if float(g[wind_detlis]) != float(j["val"]):
                                            bul = False

                                    elif x == "pressure":
                                      f = place_detalis[x]
                                      g = data_weather[y]
                                      _days_arr = {"press"}
                                      for press_detlis in _days_arr:
                                        # if g[temp_detlis] == f[temp_detlis]:
                                        j = f[press_detlis]

                                        if (j["type"] == "high"):
                                          if float(g[press_detlis]) > float(j["val"]):
                                            # return True
                                            pass
                                          else:
                                            bul = False
                                        elif (j["type"] == "low"):
                                          if float(g[press_detlis]) < float(j["val"]):
                                            pass
                                          else:
                                            bul = False
                                        elif (j["type"] == "EQ"):
                                          if float(g[press_detlis]) != float(j["val"]):
                                            bul = False

                                    elif x == "humidity":
                                      f = place_detalis[x]
                                      g = data_weather[y]
                                      j = f
                                      if (j["type"] == "high"):
                                        if float(g) > float(j["val"]):
                                          # return True
                                          pass
                                        else:
                                          bul = False
                                      elif (j["type"] == "low"):
                                        if float(g) < float(j["val"]):
                                          pass
                                        else:
                                          bul = False
                                      elif (j["type"] == "EQ"):
                                        if float(g) != float(j["val"]):
                                          bul = False

                                    elif x == "clouds":
                                      f = place_detalis[x]
                                      g = data_weather[y]
                                      j = f
                                      if (j["type"] == "high"):
                                        if float(g) > float(j["val"]):
                                          # return True
                                          pass
                                        else:
                                          bul = False
                                      elif (j["type"] == "low"):
                                        if float(g) < float(j["val"]):
                                          pass
                                        else:
                                          bul = False
                                      elif (j["type"] == "EQ"):
                                        if float(g) != float(j["val"]):
                                          bul = False

                                    if bul == False:
                                      _weather_dic.append("False")

                                    elif bul == True and is_taken == True:
                                      is_taken = False
                                      add_to_dic.append(place)
                                      add_to_dic.append(place_detalis["name"])
                                      #add_to_dic.append({'loc':place},{'name': place_detalis["name"]})
                                      #add_to_dic.append({'name': place_detalis["name"]})
                                      #_weather_data = add_to_dic.copy()
                                      _weather_dic.append(detalis_weather_data)

      self.check(_weather_dic,add_to_dic)

  def check(self, arr, more):
    data=[]
    is_false = False
    for elements in arr:
      if str(elements) != "False":
        is_false = True
        for x in elements:
          for y in range(0,len(more),2):
            x['dewpoint']=more[y]
            x['uvi']=more[y+1]
      else:
        is_false = False

    if is_false:
      pass
      pusher().push_with_random_package(f"Weather_requirements/results/user_1/", arr)
    else:
      pass
      pusher().push_with_random_package(f"Weather_requirements/results/user_1/", {"result": ":("})

    pusher().remove("/Weather_requirements/requirements/user_1/")