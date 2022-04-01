import time
import paho.mqtt.client as paho
from os import environ
from entity.sensor import Temperature, Current, Pressure, Voltage

# __________MQTT CONFIG___________
host = environ['MQTT_HOST'] if 'MQTT_HOST' in environ.keys() else "192.168.1.106"
port = environ['MQTT_PORT'] if 'MQTT_PORT' in environ.keys() else 1883
period = int(environ['MQTT_PERIOD'] if 'MQTT_PERIOD' in environ.keys() else 1)

# ________________________________

input_type = environ['TYPE'] if 'TYPE' in environ.keys() else 'temperature'
name = environ['NAME'] if 'NAME' in environ.keys() else 'sensor1'

sensors = {"temperature": Temperature, "current": Current, "pressure": Pressure, "voltage": Voltage}

sensor = sensors[input_type](name=name)

def on_publish(client, userdata, result):
    print(f"Data published: {userdata}")

client = paho.Client(sensor.name)
client.connect(host, port)

while True:
    try:
        sensor.generate_new_value()
        ret = client.publish(topic ='sensors/' + sensor.type + '/' + sensor.name, payload=sensor.get_data())
        time.sleep(period)
    except KeyboardInterrupt:
        break

