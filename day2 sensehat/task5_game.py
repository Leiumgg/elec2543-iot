from time import sleep
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

colour = [red, orange, yellow, green, blue, indigo, violet]

ball_position = [3, 3]
ball_velocity = [1, 1]
bat_pos = 4

def draw_bat(lv):
  if level >= 5:
    sense.set_pixel(0, bat_pos, colour[lv])
    sense.set_pixel(0, bat_pos+1, colour[lv])
  else:
    sense.set_pixel(0, bat_pos, colour[lv])
    sense.set_pixel(0, bat_pos+1, colour[lv])
    sense.set_pixel(0, bat_pos-1, colour[lv])
  
def move_up(event):
  global bat_pos
  if bat_pos > 1 and event.action=='pressed':
    bat_pos -= 1
    
def move_down(event):
  global bat_pos
  if bat_pos < 6 and event.action=='pressed':
    bat_pos += 1
    
def draw_ball():
  global ball_position, bounce
  # Draws the ball pixel
  sense.set_pixel(ball_position[0], ball_position[1], (255, 255, 255))
  # Moves the ball to the next position
  ball_position[0] += ball_velocity[0]
  ball_position[1] += ball_velocity[1]
    
  if ball_position[1] == 0 or ball_position[1] == 7:
    ball_velocity[1] = -ball_velocity[1]
  if ball_position[0] == 7:
    ball_velocity[0] = -ball_velocity[0]
  if ball_position[0] == 1 and bat_pos - 1 <= ball_position[1] <= bat_pos + 1:
    ball_velocity[0] = -ball_velocity[0]
    bounce += 1
        
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

level = 0
bounce = 0

while True:
  if bounce == 4:
    if level < 6:
      level += 1
    bounce = 0
  sense.clear(0, 0, 0)
  draw_bat(level)
  draw_ball()
  sleep((0.5-0.06*level))
