from firebase import firebase

class pusher():
    def __init__(self):
        self.firebase =  firebase.FirebaseApplication("https://meteo-mikoteusz-default-rtdb.firebaseio.com/", None)

    def push_with_random_package(self, direction, data):
        self.firebase.post(f"{direction}", data)

    def push_without_random_package(self, direction, data_name, value):
        y = self.firebase.put(f"{direction}",data_name, value)

    def remove(self,direction):
        self.firebase.delete(f"{direction}", None)