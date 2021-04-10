from sense_hat import SenseHat
from datetime import datetime
import time
import logging

record = open('record.txt','w')

sense = SenseHat()
sense.clear()

for i in range(50):
    date = datetime.now()
    temp = round(sense.get_temperature(), 2)
    time.sleep(1)
    record.write(str(date)+' '+str(temp)+'\r\n')  
record.close()
