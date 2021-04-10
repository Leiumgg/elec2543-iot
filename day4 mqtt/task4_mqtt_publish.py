import paho.mqtt.publish as publish

hostname = "test.mosquitto.org" 
port = 1883 

topic = "PC000/traffic_light/emergency"

status = input('emergency status?(t/f/exit) ')

while status != 'exit':
	if status == 't':
		publish.single(topic,payload = True, qos = 0, hostname = hostname, port = port)
	elif status == 'f':
		publish.single(topic,payload = False, qos = 0, hostname = hostname, port = port)
	status = input('emergency status?(t/f/exit) ')
