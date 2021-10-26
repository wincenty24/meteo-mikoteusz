from firebase import firebase

class data_fb_taker():
    def __init__(self):
        self.firebase = firebase.FirebaseApplication("https://meteo-mikoteusz-default-rtdb.firebaseio.com/", None)

    def get_saved_place(self, user):
        result = self.firebase.get(f"Search_place/{user}/Place", '')
        return result

    def get_weather_req(self):
        return self.firebase.get(f"Weather_requirements/requirements/user_1/", '')
