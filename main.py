import time
import tkinter as tk
from tkinter import ttk

from firebase import firebase
from pyowm import OWM

from data_pusher import pusher

"""
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
"""


class App():
    def __init__(self):
        self.window = tk.Tk()

        self.window.title("Python Tkinter Text Box")
        self.window.minsize(1000, 600)
        self.create_widgets()
        self.ref_time_dir = []
        self.rb_for_plce = ""
        self.forecast_taker = ""
        self._ile_label = 0
        self.ile_bylo = 0

    def create_widgets(self):
        ttk.Label(self.window, text="Temperatura:").grid(column=0, row=0)

        ttk.Label(self.window, text="z rana").grid(column=1, row=1)
        self.tem_morn = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.tem_morn).grid(column=2, row=1)
        self.tem_morn_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.tem_morn_type).grid(column=3, row=1)

        ttk.Label(self.window, text="w ciągu dnia").grid(column=1, row=2)
        self.tem_day = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.tem_day).grid(column=2, row=2)
        self.tem_day_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.tem_day_type).grid(column=3, row=2)

        ttk.Label(self.window, text="wieczorem").grid(column=1, row=3)
        self.tem_eve = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.tem_eve).grid(column=2, row=3)
        self.tem_eve_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.tem_eve_type).grid(column=3, row=3)

        ttk.Label(self.window, text="w nocy").grid(column=1, row=4)
        self.tem_night = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.tem_night).grid(column=2, row=4)
        self.tem_night_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.tem_night_type).grid(column=3, row=4)

        ttk.Label(self.window, text="odczuwalna z rana").grid(column=1, row=5)
        self.tem_feels_like_morn = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.tem_feels_like_morn).grid(column=2, row=5)
        self.tem_feels_like_morn_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.tem_feels_like_morn_type).grid(column=3, row=5)

        ttk.Label(self.window, text="odczuwalna w ciągu dnia").grid(column=1, row=6)
        self.tem_feels_like_day = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.tem_feels_like_day).grid(column=2, row=6)
        self.tem_feels_like_day_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.tem_feels_like_day_type).grid(column=3, row=6)

        ttk.Label(self.window, text="odczuwalna wieczorem").grid(column=1, row=7)
        self.tem_feels_like_eve = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.tem_feels_like_eve).grid(column=2, row=7)
        self.tem_feels_like_eve_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.tem_feels_like_eve_type).grid(column=3, row=7)

        ttk.Label(self.window, text="odczuwalna w nocy").grid(column=1, row=8)
        self.tem_feels_like_night = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.tem_feels_like_night).grid(column=2, row=8)
        self.tem_feels_like_night_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.tem_feels_like_night_type).grid(column=3, row=8)

        ttk.Label(self.window, text="minimalna").grid(column=1, row=9)
        self.tem_min = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.tem_min).grid(column=2, row=9)
        self.tem_min_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.tem_min_type).grid(column=3, row=9)

        ttk.Label(self.window, text="maksymalna").grid(column=1, row=10)
        self.tem_max = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.tem_max).grid(column=2, row=10)
        self.tem_max_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.tem_max_type).grid(column=3, row=10)
        # Output label

        ttk.Label(self.window, text="Wilgotność:").grid(column=0, row=11)
        self.hum = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.hum).grid(column=1, row=11)
        self.hum_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.hum_type).grid(column=2, row=11)

        ttk.Label(self.window, text="Ciśnienie:").grid(column=0, row=12)
        self.pres = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.pres).grid(column=1, row=12)
        self.pres_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.pres_type).grid(column=2, row=12)

        ttk.Label(self.window, text="Chmury:").grid(column=0, row=13)
        self.clouds = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.clouds).grid(column=1, row=13)
        self.clouds_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.clouds_type).grid(column=2, row=13)

        ttk.Label(self.window, text="Wiatr:").grid(column=0, row=14)
        ttk.Label(self.window, text="kierunek ").grid(column=1, row=15)
        self.deg = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.deg).grid(column=2, row=15)
        self.deg_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.deg_type).grid(column=3, row=15)

        ttk.Label(self.window, text="poryw ").grid(column=1, row=16)
        self.gust = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.gust).grid(column=2, row=16)
        self.gust_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.gust_type).grid(column=3, row=16)

        ttk.Label(self.window, text="predkosc ").grid(column=1, row=17)
        self.speed = tk.StringVar()
        ttk.Entry(self.window, width=15, textvariable=self.speed).grid(column=2, row=17)
        self.speed_type = tk.StringVar()
        ttk.Entry(self.window, width=5, textvariable=self.speed_type).grid(column=3, row=17)

        ttk.Label(self.window, text="okres czasu (rok-miesiac-dzien rok2-miesiac2-dzien2:").grid(column=0, row=19)
        self.refTime = tk.StringVar()
        ttk.Entry(self.window, width=20, textvariable=self.refTime).grid(column=2, row=19)

        self.check_box_val = tk.IntVar()
        tk.Checkbutton(self.window, text='Python', variable=self.check_box_val, onvalue=1, offvalue=0,
                       command=self.get_textbox).grid(column=0, row=21)

        ttk.Label(self.window, text="Localizacja ").grid(column=0, row=22)
        self.loc = tk.StringVar()
        self.loc_entery = ttk.Entry(self.window, width=15, textvariable=self.loc).grid(column=1, row=22)
        # c1.pack()

        button = ttk.Button(self.window, text="Click Me", command=self._clickMe)
        button.grid(column=2, row=23)

        ttk.Label(self.window, text="Rezult:").grid(column=6, row=0)

    def get_textbox(self):  ###########
        if int(self.check_box_val.get()) == 0:
            pass
            # self.loc_enteryconfig(state= 'disabled')
        else:
            pass
            # self.loc_entery.config(state='normal')

        # print(self.check_box_val.get())

    def _clickMe(self):

        self.clean(self.ile_bylo)
        owm = OWM('349af6d6cf9a308d229cf059fc3c81d6')
        mgr = owm.weather_manager()
        reg = owm.city_id_registry()
        print(self.loc.get())
        loc = reg.locations_for(str(self.loc.get()), country='PL')
        ####jeżeli chcesz po współrzędnych
        print(loc)
        location = f"{loc[0].lat}?{loc[0].lon}"
        location = location.replace(".", "-")
        self._ile_label = 0
        self.ref_time_dir = str(self.refTime.get()).split(" ")
        for index in range(0, len(self.ref_time_dir)):
            self.ref_time_dir[index] = f"{self.ref_time_dir[index]} 10:00:00+00:00"

        send = {location: {
            "clouds": {
                "type": self.clouds_type.get(),
                "val": self.clouds.get()
            },
            "humidity": {
                "type": self.hum_type.get(),
                "val": self.hum.get()
            },
            "pressure": {
                "press": {
                    "type": self.pres_type.get(),
                    "val": self.pres.get()
                }
            },
            "reference_time":
                self.ref_time_dir
            ,
            "temperature": {
                "day": {
                    "type": self.tem_day_type.get(),
                    "val": self.tem_day.get()
                },
                "eve": {
                    "type": self.tem_eve_type.get(),
                    "val": self.tem_eve.get()
                },
                "feels_like_day": {
                    "type": self.tem_feels_like_day_type.get(),
                    "val": self.tem_feels_like_day.get()
                },
                "feels_like_eve": {
                    "type": self.tem_feels_like_eve_type.get(),
                    "val": self.tem_feels_like_eve.get()
                },
                "feels_like_morn": {
                    "type": self.tem_feels_like_morn_type.get(),
                    "val": self.tem_feels_like_morn.get()
                },
                "feels_like_night": {
                    "type": self.tem_feels_like_night_type.get(),
                    "val": self.tem_feels_like_night.get()
                },
                "max": {
                    "type": self.tem_max_type.get(),
                    "val": self.tem_max.get()
                },
                "min": {
                    "type": self.tem_min_type.get(),
                    "val": self.tem_min.get()
                },
                "morn": {
                    "type": self.tem_morn_type.get(),
                    "val": self.tem_morn.get()
                },
                "night": {
                    "type": self.tem_night_type.get(),
                    "val": self.tem_night.get()
                }
            },
            "wind": {
                "deg": {
                    "type": self.speed_type.get(),
                    "val": self.speed.get()
                },
                "gust": {
                    "type": self.gust_type.get(),
                    "val": self.gust.get()
                },
                "speed": {
                    "type": self.speed_type.get(),
                    "val": self.speed.get()
                },
            },
            "name": "HEllo",
        }}
        pusher().push_with_random_package(f"Weather_requirements/requirements/user_1/", send)
        self.show_data_form_results()
        pusher().remove("/Weather_requirements/")

    def show_data_form_results(self):
        time.sleep(4)
        self.forecast_taker = forecast_taker()
        while (True):
            self.forecast_taker.take_it()
            print("ref", self.forecast_taker.result)
            if (
                    self.forecast_taker.result != ":(" and self.forecast_taker.result != "None") and self.forecast_taker.how_many_days != 'heszke':

                index = self.forecast_taker.how_many_days
                self.ile_bylo = index
                print("index", index)
                for t in range(0, index):
                    print("t1", t)
                    self.show(t)
                break
            elif self.forecast_taker.result == "None" or self.forecast_taker.result == ":(":
                for t in range(0, self.ile_bylo):
                    print("t1", t)
                    self.clean(t)
                ttk.Label(self.window, text=f"Nie znalazłem").grid(column=6, row=self._ile_label)
                self.ile_bylo = 0
                break

            else:
                print("brejk")
                break
            time.sleep(3)

    def show(self, index):
        # jest zmienna _ile_label, która określa jak dużo jest poniższych labeli
        print(index, "tttt")
        ttk.Label(self.window, text=f"Czas: {self.forecast_taker.ref_time[index]}").grid(column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Temperatura z rana: {self.forecast_taker.tem_morn[index]} st.C").grid(column=6,
                                                                                                            row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Temperatura w dzień: {self.forecast_taker.tem_day[index]} st.C").grid(column=6,
                                                                                                            row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Temperatura wieczorem: {self.forecast_taker.tem_eve[index]} st.C").grid(column=6,
                                                                                                              row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Temperatura w nocy: {self.forecast_taker.tem_night[index]} st.C").grid(column=6,
                                                                                                             row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window,
                  text=f"Temperatura odczuwalna z rana: {self.forecast_taker.tem_feels_like_morn[index]} st.C").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window,
                  text=f"Temperatura odczuwalna w dzień: {self.forecast_taker.tem_feels_like_day[index]} st.C").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window,
                  text=f"Temperatura odczuwalna wieczorem: {self.forecast_taker.tem_feels_like_eve[index]} st.C").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window,
                  text=f"Temperatura odczuwalna w nocy: {self.forecast_taker.tem_feels_like_night[index]} st.C").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Maksymalna temperatura: {self.forecast_taker.tem_max[index]} st.C").grid(column=6,
                                                                                                               row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Minimalna temperatura: {self.forecast_taker.tem_night[index]} st.C").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Zachmurzenie: {self.forecast_taker.clouds[index]}").grid(column=6,
                                                                                               row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Wilgotność: {self.forecast_taker.humidity[index]} g/m3").grid(column=6,
                                                                                                    row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Ciśnienie: {self.forecast_taker.pressure[index]} hPa").grid(column=6,
                                                                                                  row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Opady deszczu: {self.forecast_taker.rain[index]}").grid(column=6,
                                                                                              row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Prędkość wiatru: {self.forecast_taker.wind_speed[index]} km/h").grid(column=6,
                                                                                                           row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Zryw wiatru: {self.forecast_taker.wind_gust[index]}").grid(column=6,
                                                                                                 row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text=f"Kierunek wiatru: {self.forecast_taker.wind_deg[index]}").grid(column=6,
                                                                                                    row=self._ile_label)
        self._ile_label = self._ile_label + 1

    def clean(self, index):
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6,
            row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6,
            row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6,
            row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6,
            row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window,
                  text="                                                                    ").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window,
                  text="                                                                    ").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window,
                  text="                                                                    ").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6,
            row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6,
            row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6,
            row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6,
            row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6,
            row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                    ").grid(
            column=6,
            row=self._ile_label)
        self._ile_label = self._ile_label + 1
        ttk.Label(self.window, text="                                                                       ").grid(
            column=6, row=self._ile_label)
        self._ile_label = self._ile_label + 1


class forecast_taker:
    def __init__(self):
        self.firebase = firebase.FirebaseApplication("https://meteo-mikoteusz-default-rtdb.firebaseio.com/", None)
        self.temp = self.firebase.get(f"Weather_requirements/results/user_1/", '')
        print("ewqeq", self.temp)
        self.clouds = []
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
        self.status = []
        self.result = ""

    def take_it(self):
        self.how_many_days = "heszke"
        if self.temp != None and self.temp != "" and str(self.temp) != "None":
            print("temp", self.temp)
            for x in self.temp:
                self.how_many_days = len(self.temp[x])
                cout = 0
                for y in self.temp[x]:
                    print("igerk", y)
                    if y != "result":
                        for z in y:

                            for c in z:
                                for c in z:
                                    if c == "clouds":
                                        self.clouds.append(str(z['clouds']))
                                    else:
                                        self.clouds.append(str(0))

                                self.detailed_status.append(z['detailed_status'])
                                self.point.append(str(z['dewpoint']))
                                self.humidity.append(str(z['humidity']))
                                for c in z:
                                    if c == "press":
                                        _pres = z['pressure']
                                        self.pressure.append(str(_pres['press']))
                                    else:
                                        self.pressure.append(str(0))

                                if c == "rain":
                                    _rain = z['rain']
                                    self.rain.append(str(_rain['all']))
                                else:
                                    self.rain.append(str(0))

                                self.ref_time.append(str(z['reference_time']))
                                self.status.append(str(z['status']))
                                self.sunrise_time.append(str(z['sunrise_time']))
                                self.sunset_time.append(str(z['sunset_time']))
                                _tem = z['temperature']
                                self.tem_day.append(str(_tem['day']))
                                self.tem_eve.append(str(_tem['eve']))
                                self.tem_feels_like_day.append(str(_tem['feels_like_day']))
                                self.tem_feels_like_eve.append(str(_tem['feels_like_eve']))
                                self.tem_feels_like_morn.append(str(_tem['feels_like_morn']))
                                self.tem_feels_like_night.append(str(_tem['feels_like_night']))
                                self.tem_max.append(str(_tem['max']))
                                self.tem_min.append(str(_tem['min']))
                                self.tem_morn.append(str(_tem['morn']))
                                self.tem_night.append(str(_tem['night']))
                                if c == "wind":
                                    _wind = z['wind']
                                    self.wind_deg.append(str(_wind['deg']))
                                    self.wind_gust.append(str(_wind['gust']))
                                    self.wind_speed.append(str(_wind['speed']))
                                else:
                                    self.wind_deg.append(str(0))
                                    self.wind_gust.append(str(0))
                                    self.wind_speed.append(str(0))

                    else:
                        self.result = ":("
        else:
            self.result = "None"

        print(" self.result ", self.result)


if __name__ == "__main__":
    app = App()
    app.window.mainloop()
