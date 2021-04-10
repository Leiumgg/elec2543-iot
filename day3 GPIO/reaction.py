import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

left_player = input('Please enter the left play name:')
right_player = input('Please enter the right play name:')

led = 4
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, 0)
time.sleep(random.uniform(1, 5))
GPIO.output(led, 1)

left_button = 14
right_button = 15

GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)

try:
    while True:
        if (GPIO.input(14)) == False:
            print(left_player, 'wins!')
            break
        if (GPIO.input(15)) == False:
            print(right_player, 'wins!')
            break

except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()

