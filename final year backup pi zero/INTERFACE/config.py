from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.textinput import TextInput
from functools import partial
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import kivy
from kivy.config import Config
Config.set('graphics', 'resizable', True)
kivy.require('1.9.0')
from kivy.uix.image import Image

def conf(crop):
    global cropd
    cropd=crop
    SpinnerExample().run()

class SpinnerExample(App):
    def build(self):
        weight = []

        weight.append(str(50)+" Grams")
        weight.append(str(100)+" Grams")
        weight.append(str(150)+" Grams")
        weight.append(str(200)+" Grams")
        
        layout = FloatLayout()

        img = Image(source="theam1.jpg", 
        pos=(0, 0),
        size=(1540, 1920), #, <- CRUCIAL setting this will
        #size_hint=(None, None)
        pos_hint={"x": .0, "y": .0})
        layout.add_widget(img)
        
        self.spinnerObject = Spinner(text="Select Weight", values=(
            weight), background_color=(0.784, 0.443, 0.216, 1))
        self.spinnerObject.size_hint = (0.27, 0.07)
        self.spinnerObject.pos_hint = {'x': .35, 'y': .55}
        self.spinnerObject.size = (10, 4)

        def show_selected_value(spinner, text):
            time = []
            for word in text.split():
                if word.isdigit():
                    selectedweight=word
            caltime=int(selectedweight)+int(cropd)
            print(caltime)
##            for i in range(1, 5):
##                time.append(str(i)+" Day")
##            self.spinnerObject1 = Spinner(text=str(caltime)+' day', values=(
##                time), background_color=(0.784, 0.443, 0.216, 1))
##            self.spinnerObject1.size_hint = (0.27, 0.07)
##            self.spinnerObject1.pos_hint = {'x': .35, 'y': .45}
##            print()

            drying_level = ['High', 'Medium', 'Low']
            self.spinnerObject2 = Spinner(text="Drying level", values=(
                drying_level), background_color=(0.784, 0.443, 0.216, 1))
            self.spinnerObject2.size_hint = (0.27, 0.07)
            self.spinnerObject2.pos_hint = {'x': .35, 'y': .45}

            def show_selected_value2(spinner, text5):
                self.btn = Button(text="",
                color=(1, 0, .65, 1),
                background_normal='start.jpg',
                size_hint=(.2, .2),
                pos_hint={"x": 0.40, "y": 0.20})
                def a():
                    layout.clear_widgets()
                    App().get_running_app().stop()
                    import Activity
                    Activity.act()
                self.btn.bind(on_press=lambda x: a())
                layout.add_widget(self.btn)

           # |
            self.spinnerObject2.bind(text=show_selected_value2)
            layout.add_widget(self.spinnerObject2)

        
       # |
        self.spinnerObject.bind(text=show_selected_value)
        layout.add_widget(self.spinnerObject)
        return layout;


