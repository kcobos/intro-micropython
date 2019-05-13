import time
from umqtt.simple import MQTTClient

c = MQTTClient("ESP8266", "cubie.kcobos.es")
if not c.connect():
    print("Conectando")

i=0
while True:
    c.publish("prueba", "contando "+str(i))
    time.sleep(1)
    i+=1

c.disconnect()