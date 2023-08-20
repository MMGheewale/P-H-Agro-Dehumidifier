import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.video import Video

import RPi.GPIO as GPIO
import time
import random
from threading import Thread


class ActivityLab(App):
    def build(self):
        layout = FloatLayout()

        img = Image(source="theam.jpg", 
        pos=(0, 0),
        size=(1540, 1920), #, <- CRUCIAL setting this will
        #size_hint=(None, None)
        pos_hint={"x": .0, "y": .0})
        layout.add_widget(img)
        
        self.main_text = Label(pos_hint={"x": 0.40, "y": 0.40})
        
        layout.add_widget(self.main_text)
        

        def update(val):
            self.main_text.text = val
            
        def control():
            TEMP=32
            HUM=50

            ON=False
            OFF=True

            fantop=22
            fandown=27
            motor=17

            GPIO.setmode(GPIO.BCM)
            GPIO.setup(fantop,GPIO.OUT)
            GPIO.setup(fandown,GPIO.OUT)
            GPIO.setup(motor,GPIO.OUT)

            GPIO.output(fandown,OFF)
            GPIO.output(motor,OFF)

            GPIO.output(fantop,ON)
            time.sleep(5)

            fantoplastTime = time.time()
            motorlastTimer = time.time()
            last_Timer = time.time()
            time.process_time
            
            update(str(29))

            while True:
                if(((time.time()-fantoplastTime) >=0) and (((time.time()-fantoplastTime) <=9)) and ((time.time()-last_Timer)<59)):
                    GPIO.output(fantop,ON)
                if(((time.time()-fantoplastTime) >=10)  and ((time.time()-fantoplastTime) <=14) and ((time.time()-last_Timer)<59)):
                    GPIO.output(fantop,OFF)
                if(((time.time()-fantoplastTime) >= 15)  and ((time.time()-last_Timer)<59)):
                    fantoplastTime=time.time()
                    GPIO.output(fantop,OFF)
                if(((time.time()-last_Timer)>=60) and ((time.time()-last_Timer)<=70)):
                    update(str(31))
                    print("Exhaust on \n heating off\n")
                    GPIO.output(fantop,OFF)
                    GPIO.output(fandown,ON)
                if((time.time()-last_Timer)>=71):
                    update(str(30))
                    print("Exhaust off \n heating on\n")
                    GPIO.output(fandown,OFF)
                    last_Timer=time.time()
                    fantoplastTime=time.time()


                if((time.time()-motorlastTimer) <=2):
                    GPIO.output(motor,ON)
                if(((time.time()-motorlastTimer) >=10) and ((time.time()-motorlastTimer) <=12)):
                    GPIO.output(motor,OFF)
                if((time.time()-motorlastTimer) >=12):
                    motorlastTimer=time.time()
   
        get_level_thread = Thread(target = control)
      
        get_level_thread.daemon = True
        get_level_thread.start()  

        return layout
  
label = ActivityLab()
def act():
    label.run()
