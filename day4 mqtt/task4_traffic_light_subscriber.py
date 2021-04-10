import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import random
hostname = 'test.mosquitto.org'
port = 1883

topic = 'PC000/traffic_light/emergency'

def on_connect(client, userdata, flags, rc):
	print('Connection result: ' + str(rc))
	if rc == 0:
		client.subscribe(topic)

def on_publish(client, userdata, mid):
	print('[MQTT] Sent: ' + str(mid))

def on_message(client, userdata, message):
    global message_received
    time.sleep(0.25)
    print('Received message on',message.topic,':',message.payload.decode('utf-8'),'qos =',str(message.qos))
    message_received = str(message.payload.decode('utf-8'))
    
def on_disconnect(client, userdata, rc):
	if rc != 0:
		print('Disconnected unexpectedly')

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_message = on_message
mqttc.on_disconnect = on_disconnect
mqttc.connect(hostname, port = port, keepalive = 60, bind_address = '')
mqttc.loop_start()


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
    publish.single(topic, payload = 'State 1', qos = 0, hostname = hostname, port = port)
    time.sleep(5)
    publish.single(topic, payload = 'State 2', qos = 0, hostname = hostname, port = port)
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
    publish.single(topic, payload = 'State 3', qos = 0, hostname = hostname, port = port)
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

m = False

while True:
    if m == True:
        GPIO.output(red, 0)
        GPIO.output(green, 0)
        GPIO.output(signal, 1)
        time.sleep(0.5)
        GPIO.output(signal, 0)
        time.sleep(0.5)
    elif m == False:
        GPIO.output(red, 0)
        GPIO.output(signal, 0)
        greenlight(green)
        GPIO.output(green, 0)
        redtosignal(red, signal)
    m = message_received
