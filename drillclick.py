from pynput.mouse import Button, Controller
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
mouse = Controller()
x = 1 
GPIO.setup(12,GPIO.OUT) 
GPIO.setup(3, GPIO.IN, 
pull_up_down=GPIO.PUD_UP) 

while True:
    state1 = GPIO.input(3)
    if state1 == False: 
        GPIO.output(12,GPIO.HIGH) 
        print("on")
        x += 1
        if x == 2:
            mouse.press(Button.left)
            mouse.release(Button.left)
            x -= 1
    if state1 == True:
        GPIO.output(12,GPIO.LOW)
