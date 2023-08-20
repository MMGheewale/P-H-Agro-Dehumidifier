import kivy
from kivy.config import Config 
Config.set('graphics', 'resizable', True)  	
from kivy.app import App 
kivy.require('1.9.0') 
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from functools import partial
from kivy.uix.video import Video
import time
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty

class SpinnerExample(App):
        def build(self):
                layout = FloatLayout()
                video = Video(source='main.mp4')
                video.state='play'
                video.allow_stretch=True
                self.btn = Button(text="",
                color=(1, 0, .65, 1),
                background_normal='start.png',
                size_hint=(.2, .2),
                pos_hint={"x": 0.85, "y": 0.10})
                def on_position_change(instance, value):
                    print('The position in the video is', value)
                    if(int(value+0.4) == 7):
                      video.state='stop'    
                      print("time")
                      layout.clear_widgets()
                      App().get_running_app().stop()
                      import maize
                      maize.maz()
                video.bind(position=on_position_change)
                layout.add_widget(video)
                return layout; 

def maz():
        SpinnerExample().run()

maz()
