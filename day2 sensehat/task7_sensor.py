from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temp = round(sense.get_temperature(),2)

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            print(temp)
