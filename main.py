


from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Color
from kivy.app import App
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

from kivy.uix.popup import Popup

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


from kivy.uix.button import Button




class Main(App):
    def build(self):
        return self.constructBox()

    def constructBox(self):
        self.box   = BoxLayout(orientation='vertical')
        self.box.add_widget(Label(text="TATA"))
        # mapwindow = FAFA
        # self.box.add_widget(self.plotter.constructWidget())

        Window.bind(on_key_down=self.keypress)
        # Clock.schedule_interval(self.update, 0.2)
        return self.box

    def keypress(self,frame, keyboard, keycode, key, modifiers):
        pass

Main().run()
