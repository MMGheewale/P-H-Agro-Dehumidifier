import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.video import Video

class ActivityLab(App):
    def build(self):
        layout = FloatLayout()

        video = Video(source='loding.mp4')
        video.state='play'
        video.allow_stretch=True
        video.options = {'eos': 'loop'}
        layout.add_widget(video)

        self.label = Label(text='''Remaining Time: 1 Day 23 Hours 59 Min
                          \nDay/Night: Day
                          \nCurrent consumption: 0.001 Unit
                          \nProgress: 1%
                           ''')
        layout.add_widget(self.label)
        return layout
  
label = ActivityLab()
def act():
    label.run()
