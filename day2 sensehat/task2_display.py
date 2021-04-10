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

colour = [red, orange, yellow, green, blue, indigo, violet, white]

while True:
  for i in range(len(colour)-1):
    sense.show_message("EEE is awesome!", text_colour=colour[i], back_colour=colour[i-1], scroll_speed=0.05)
