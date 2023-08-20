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
import random

class SpinnerExample(App):
        def build(self):
                layout = FloatLayout()
                
                self.main_text = Label()
                layout.add_widget(self.main_text)

                def update(val):
                    self.main_text.text = val

                update(str(32))
        
                    
                return layout; 

def maz():
        SpinnerExample().run()

maz()
