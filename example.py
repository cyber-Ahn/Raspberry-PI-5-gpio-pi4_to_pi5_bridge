#import RPi.GPIO as GPIO
import TGNgpio as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 17 #pin 11
GPIO.setup(led,GPIO.OUT)

print("LED on")
GPIO.output(led,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(led,GPIO.LOW)

button = 27 #pin 13
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if GPIO.input(button) == GPIO.HIGH:
    print("Button was pushed!")
else:
    print("Button not pressed")
