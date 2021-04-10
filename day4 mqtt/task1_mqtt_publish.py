import paho.mqtt.publish as publish

hostname = "test.mosquitto.org" 
port = 1883 

topic = "3035683265/test"

publish.single(topic,payload = "Hello,elec2840!", qos = 0, hostname = hostname, port = port)
