


from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


import requests
import json
import urllib
import geocoder
import io
import PIL
import urllib
# from PIL import Image, ImageDraw, ImageFont




class LocalInfo(BoxLayout):
    orientation = "vertical"
    lat,lng = 0,0
    APIKEY      = "AIzaSyABY9PJX_0ScAy6Sdtv3_bMa5qmOpL_ZBc"
    mapboxKEY   = "pk.eyJ1IjoiYXVndXN0Z2UiLCJhIjoiY2s4YTJyNHYwMGNoNjNscWw5bHc5cGhoeiJ9.AxRUBI4Qd_Zgv-lyPnv2SA"
    queryString = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{long}&radius={radius}&type={type}&key={APIKEY}{pagetoken}"
    mapboxQs    = "https://api.mapbox.com/styles/v1/mapbox/{style}/static/{lon},{lat},{zoom}/{w}x{h}{retina}?access_token={token}&attribution={attribution}&logo=false"
    staticMapQuery = "http://www.mapquestapi.com/staticmap/v4/getmap"


    def __init__(self, **kwargs):
        super(LocalInfo, self).__init__(**kwargs)
        self.info = Label(text="tototot")
        self.add_widget(self.info)
        self.getPosition()
        self.getLocalInfo()
        self.getStaticMapAround()
        self.info.text += "\n"
        for place in self.localPlaces:
            self.info.text += place["name"] + "\n"
        # with self.canvas:
        #     Color(.234, .456, .678, .8)  # set the colour
        #     self.rect = Rectangle(size =(100,100))

    def getPosition(self):
        g = geocoder.ip('me')
        self.lat, self.long  = g.latlng
        self.info.text = "lat:%.4f long:%.4f"%(self.lat, self.long)

    def getLocalInfo(self,type="restaurant",radius=300,pagetoken=None):
        pagetoken = "&pagetoken="+pagetoken if pagetoken else ""
        url = self.queryString.format(  lat=self.lat,long=self.long,
                                        radius=radius,type=type,
                                        APIKEY=self.APIKEY,
                                        pagetoken=pagetoken)
        response = requests.get(url)
        res = json.loads(response.text)
        self.localPlaces = res["results"]

    def getStaticMapAround(self,zoom=14):
        url = self.mapboxQs.format(style="streets-v10",lat=self.lat,lon=self.long,zoom=zoom,w=400,h=400,retina="",token=self.mapboxKEY,attribution="true")
        with urllib.request.urlopen(url) as response:
            data = io.BytesIO(response.read())
            data.seek(0)
            self.img = CoreImage(data, ext='png')
            self.IMG = Image(texture=self.img.texture)
            self.add_widget(self.IMG)


class Main(App):
    def build(self):
        return self.constructBox()

    def constructBox(self):
        self.box   = BoxLayout(orientation='vertical')
        self.box.add_widget(Label(text="TATA",size_hint=(1,0.05)))
        self.mapwindow = LocalInfo()
        self.box.add_widget(self.mapwindow)

        Window.bind(on_key_down=self.keypress)
        # Clock.schedule_interval(self.update, 0.2)
        return self.box

    def keypress(self,frame, keyboard, keycode, key, modifiers):
        pass



Main().run()
