from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()

ball_position = [random.randint(0, 7), random.randint(0, 7)]
colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
sense.set_pixel(ball_position[0], ball_position[1], colour)
current_colour = colour
current_position = ball_position

while True:
  flag = 1
  sleep(1)
  while current_colour == colour or colour == (0, 0, 0):
    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  while flag == 1:
    ball_position[0] = ball_position[0] + random.randint(-1, 1)
    ball_position[1] = ball_position[1] + random.randint(-1, 1)
    ball_position = [ball_position[0], ball_position[1]]
    if ball_position == current_position or ball_position[0] > 7 or ball_position[0] < 0 or ball_position[1] > 7 or ball_position[1] < 0:
      flag = 1
      ball_position = [current_position[0], current_position[1]]
    else:
      flag = 0
  sense.clear()
  sense.set_pixel(ball_position[0], ball_position[1], colour)
  current_colour = colour
  current_position = [ball_position[0], ball_position[1]]
