


from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


import requests
import json
import urllib
import ssl


import geocoder


class LocalInfo(BoxLayout):
    # lat,lng =
    APIKEY = "AIzaSyABY9PJX_0ScAy6Sdtv3_bMa5qmOpL_ZBc"
    queryString = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={APIKEY}{pagetoken}"

    def __init__(self, **kwargs):
        super(LocalInfo, self).__init__(**kwargs)
        with self.canvas:
            Color(.234, .456, .678, .8)  # set the colour
            self.rect = Rectangle(size =(100,100))

    def getPosition(self):
        g = geocoder.ip('me')
        self.lat, self.lng  = g.latlng

    def getLocalInfo(self,lat,lng,type="restaurant",radius=300,pagetoken=None):
        url = self.queryString.format(
                        lat=self.lat,lng=self.lng,radius=radius,type=type,APIKEY=self.APIKEY,pagetoken="&pagetoken="+pagetoken if pagetoken else "")
        response = requests.get(url)
        res = json.loads(response.text)
        for result in res["results"]:
            print(result["name"])
            for key in result:
              print(" --",key,result[key])



class Main(App):
    def build(self):
        return self.constructBox()

    def constructBox(self):
        self.box   = BoxLayout(orientation='vertical')
        self.box.add_widget(Label(text="TATA"))
        self.mapwindow = LocalInfo()
        self.box.add_widget(self.mapwindow)

        Window.bind(on_key_down=self.keypress)
        # Clock.schedule_interval(self.update, 0.2)
        return self.box

    def keypress(self,frame, keyboard, keycode, key, modifiers):
        pass



Main().run()
