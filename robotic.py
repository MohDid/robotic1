import RPi.GPIO as GPIO
from time import sleep
 


	
def init_capteur():
	TRIG = 7 
	ECHO = 12
	print "distance Measurement In Progress"

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

	GPIO.output(TRIG,False)

	print "Waiting for  Sensor To settle"

	return;
def check_distance():
	TRIG = 7 
	ECHO = 12

	GPIO.output(TRIG,True)
	sleep (0.00001)
	GPIO.output(TRIG, False)
	while GPIO.input(ECHO) ==0:
		pulse_start = time.time()
	while GPIO.input(ECHO) ==1:
		pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)

	return distance;

 
 


def init_moteur(): 
	Motor1A = 16
	Motor1B = 18
	Motor1E = 22
	
	Motor2A = 15
	Motor2B = 13
	Motor2E = 11
	
	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)
	
	GPIO.setup(Motor2A,GPIO.OUT)
	GPIO.setup(Motor2B,GPIO.OUT)
	GPIO.setup(Motor2E,GPIO.OUT)
	return;
	
def avancer():
	print "Going forwards"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)
	
	return;
def reculer():	
	print "Going backwards"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
	
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)

	return;
	
def droite():
	print "Going right"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
	
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)
	return;
def gauche():
	print "Going left"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
	return;
def stop():
	print "Now stop"
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)
	return;
	
GPIO.setmode(GPIO.BOARD)
init_capteur()
init_moteur()
while True: 	
	distance = check_distance()

	if (distance >= 10):
		avancer()
		sleep(1)
	else:
		while (distance >= 10):
			droite()
			distance = check_distance()
		avancer()
		sleep(1)
GPIO.cleanup()

	
