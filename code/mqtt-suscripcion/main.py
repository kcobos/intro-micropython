from umqtt.simple import MQTTClient

def sub_cb(topic, msg):
    print((topic, msg))

c = MQTTClient("ESP8266", "cubie.kcobos.es")
c.set_callback(sub_cb)
c.connect()
print("Conectando")
c.subscribe(b"prueba")
print("Suscrito a prueba")

while True:
    c.wait_msg()

c.disconnect()