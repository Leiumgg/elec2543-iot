import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

signal = 4
red = 17
green = 27
wait = 22

GPIO.setup(signal,GPIO.OUT)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(wait,GPIO.IN,GPIO.PUD_UP)

def wait_button(wait):
    while True:
        if GPIO.input(wait) == False:
            start_time = time.time()
            while (GPIO.input(wait))==False:
                pass
            end_time = time.time()
            interval = end_time - start_time
            return interval

def pressed(interval):
    if interval >= 0.5:
        return True

def greenlight(green):
    GPIO.output(green, 1)
    time.sleep(5)
    for i in range(6):
        if i % 2 == 0:
            GPIO.output(green, 1)
            time.sleep(0.5)
        else:
            GPIO.output(green, 0)
            time.sleep(0.5)

def redtosignal(red, signal):
    initial = time.time()
    GPIO.output(red, 1)
    interval = wait_button(wait)
    flag = 0
    while flag == 0:
        if pressed(interval) == True:
            flag = 1
    final = time.time()
    diff = final - initial
    if diff < 5:
        GPIO.output(signal, 1)
        time.sleep((5-diff)+3)
    else:
        GPIO.output(signal, 1)
        time.sleep(3)

try:
    while True:
        GPIO.output(red, 0)
        GPIO.output(signal, 0)
        greenlight(green)
        GPIO.output(green, 0)
        redtosignal(red, signal)

except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()

