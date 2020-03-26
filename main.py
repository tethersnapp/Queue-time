


from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.button import Button
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


import requests
import json
import urllib
import ssl


import geocoder


class LocalInfo(Widget):
    APIKEY = "AIzaSyBXYaJf79P51MqE6JXZjfZohBUnpuV1RyU"
    queryString = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={APIKEY}{pagetoken}"
    USER_AGENT = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/54.0.2840.98 Safari/537.36"}
    def __init__(self, **kwargs):
        super(LocalInfo, self).__init__(**kwargs)

    def getPosition(self):
        pass

    def getLocalInfo(self,lat,lng,type="restaurant",radius=300,pagetoken=None):
        url = self.queryString.format(
                        lat = lat,lng = lng, radius = radius, type = type,APIKEY = self.APIKEY, pagetoken = "&pagetoken="+pagetoken if pagetoken else "")
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

# g = geocoder.ip('me')
# lat, lng    = g.latlng
# LI = LocalInfo()
# LI.getLocalInfo(lat,lng)

Main().run()
