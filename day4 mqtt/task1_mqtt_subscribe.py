import paho.mqtt.client as mqtt

hostname = 'test.mosquitto.org'
port = 1883

topic = '3035683265/#'

def on_connect(client, userdata, flags, rc):
	print('Connection result: ' + str(rc))
	if rc == 0:
		client.subscribe(topic)

def on_message(client, userdata, message):
	print('Received message on %s: %s (QoS = %s)' % (message.topic, message.payload.decode('utf-8'), str(message.qos)))

def on_disconnect(client, userdata, rc):
	if rc != 0:
		print('Disconnected unexpectedly')
		
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect(hostname, port=port)

client.loop_forever()
