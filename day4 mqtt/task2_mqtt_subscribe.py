import paho.mqtt.client as mqtt

hostname = 'test.mosquitto.org'
port = 1883

topic = 'PC000/#'

def on_connect(client, userdata, flags, rc):
	print('Connection result: ' + str(rc))
	if rc == 0:
		client.subscribe(topic)

def on_publish(client, userdata, mid):
	print('[MQTT] Sent: ' + str(mid))

def on_message(client, userdata, message):
	print('Received message on %s: %s (QoS = %s)' % (message.topic, message.payload.decode('utf-8'), str(message.qos)))

def on_disconnect(client, userdata, rc):
	if rc != 0:
		print('Disconnected unexpectedly')
		
mqttc = mqtt.Client()

mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_message = on_message
mqttc.on_disconnect = on_disconnect

mqttc.connect(hostname, port = port, keepalive = 60, bind_address='')


mqttc.loop_forever()
