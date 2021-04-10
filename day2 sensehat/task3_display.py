from random import choice
from sense_hat import SenseHat
sense = SenseHat()

violet = (148, 0, 211)
indigo = (75, 0, 130)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
orange = (255, 127, 0)
red = (255, 0, 0)
white = (255, 255, 255)

colour = [violet, indigo, blue, green, yellow, orange, red, white]

while True:
  bg_colour = choice(colour)
  t_colour = choice(colour)
  sense.show_message("EEE is awesome!", text_colour=t_colour, back_colour=bg_colour, scroll_speed=0.05)  
