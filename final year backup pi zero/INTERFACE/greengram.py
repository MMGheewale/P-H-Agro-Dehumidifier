import kivy
from kivy.config import Config 
Config.set('graphics', 'resizable', True)  	
from kivy.app import App 
kivy.require('1.9.0') 
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from functools import partial
import config
from kivy.uix.image import Image

class SpinnerExample(App):
        
        def build(self):
                layout = FloatLayout()

                img = Image(source="theam1.jpg", 
                pos=(0, 0),
                size=(1540, 1920), #, <- CRUCIAL setting this will
                #size_hint=(None, None)
                pos_hint={"x": .0, "y": .0})
                layout.add_widget(img)

                self.btn = Button(text ="", 
	        color =(1, 0, .65, 1), 
	        background_normal = 'greengram.jpg', 
	        background_down ='down.jpg',
                size_hint = (.4, .7),
	        pos_hint = {"x":0.30, "y":0.2}) 
                def e():
                        layout.clear_widgets()
                        App().get_running_app().stop()
                        config.conf(2)
                self.btn.bind(on_press=lambda x: e())
                layout.add_widget(self.btn)


                self.btn1 = Button(text ="", 
	        color =(1, 0, .65, 1), 
	        background_normal = 'right.jpg', 
	        background_down ='down.jpg',
                size_hint = (.2, .2),
	        pos_hint = {"x":0.72, "y":0.455}) 
                def f():
                        layout.clear_widgets()
                        App().get_running_app().stop()
                        import main
                        main.maz()
                self.btn1.bind(on_press=lambda x: f())
                layout.add_widget(self.btn1)


                self.btn2 = Button(text ="", 
	        color =(1, 0, .65, 1), 
	        background_normal = 'left.jpg', 
	        background_down ='down.jpg',
                size_hint = (.2, .2),
	        pos_hint = {"x":0.12, "y":0.455}) 
                def g():
                        layout.clear_widgets()
                        App().get_running_app().stop()
                        import main
                        maize.maz()
                self.btn2.bind(on_press=lambda x: g())
                layout.add_widget(self.btn2)
        
                return layout; 

def sun():
        SpinnerExample().run()
