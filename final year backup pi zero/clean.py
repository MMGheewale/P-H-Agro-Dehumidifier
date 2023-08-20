import RPi.GPIO as GPIO
import time

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

GPIO.cleanup()