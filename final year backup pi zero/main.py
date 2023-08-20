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

GPIO.output(fandown,OFF)
GPIO.output(motor,OFF)

GPIO.output(fantop,ON)
time.sleep(5)

fantoplastTime = time.time()
motorlastTimer = time.time()
last_Timer = time.time()
time.process_time

while True:
	if(((time.time()-fantoplastTime) >=0) and (((time.time()-fantoplastTime) <=9)) and ((time.time()-last_Timer)<59)):
		GPIO.output(fantop,ON)
	if(((time.time()-fantoplastTime) >=10)  and ((time.time()-fantoplastTime) <=14) and ((time.time()-last_Timer)<59)):
		GPIO.output(fantop,OFF)
	if(((time.time()-fantoplastTime) >= 15)  and ((time.time()-last_Timer)<59)):
		fantoplastTime=time.time()
		GPIO.output(fantop,OFF)
	if(((time.time()-last_Timer)>=60) and ((time.time()-last_Timer)<=70)):
		TEMP=34
		print("Exhaust on \n heating off\n")
		GPIO.output(fantop,OFF)
		GPIO.output(fandown,ON)
	if((time.time()-last_Timer)>=71):
		TEMP=32
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

