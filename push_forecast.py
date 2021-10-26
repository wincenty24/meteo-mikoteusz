##ten plik należy podzielić na 2 segementy. Na wpisywanie danych oraz ich wysyłanie
#wpisywanie danych
#pobierz biblotekę  OWM

from data_pusher import  pusher
from pyowm import OWM

###### jeżeli chcesz wyszukać po miejscowości
place="Warsaw"
owm = OWM('349af6d6cf9a308d229cf059fc3c81d6')
mgr = owm.weather_manager()
reg = owm.city_id_registry()
loc = reg.locations_for(place, country='PL')
####jeżeli chcesz po współrzędnych

location=f"{loc[0].lat}?{loc[0].lon}"
location=location.replace(".", "-")
#52-229771?21-01178
print(location)
val ={location: {
      "clouds": {
        "type": "N",
        "val": 9
      },
      "humidity": {
        "type": "N",
        "val": 46
      },
      "pressure": {
        "press": {
          "type": "N",
          "val": 1014
        }
      },
      "reference_time": [
        "2021-06-26 10:00:00+00:00",
        "2021-05-27 10:00:00+00:00",
      ],
      "temperature": {
        "day": {
          "type": "high",
          "val": 10
        },
        "eve": {
          "type": "N",
          "val": 23.19
        },
        "feels_like_day": {
          "type": "N",
          "val": 22.13
        },
        "feels_like_eve": {
          "type": "N",
          "val": 22.58
        },
        "feels_like_morn": {
          "type": "N",
          "val": 12.58
        },
        "feels_like_night": {
          "type": "N",
          "val": 12.58
        },
        "max": {
          "type": "N",
          "val": 23.86
        },
        "min": {
          "type": "N",
          "val": 7.95
        },
        "morn": {
          "type": "N",
          "val": 13.12
        },
        "night": {
          "type": "N",
          "val": 17.18
        }
      },
      "wind": {
        "deg": {
          "type": "n",
          "val": 140
        },
        "gust": {
          "type": "n",
          "val": 53.82
        },
        "speed": {
          "type": "n",
          "val": 26.856
        },
      },
      "name": "Warszawa",
    }
  }



pusher().push_with_random_package(f"/Weather_requirements/requirements/user_1/",val)