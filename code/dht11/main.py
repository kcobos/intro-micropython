import machine
import dht
d = dht.DHT11(machine.Pin(5))
d.measure()
d.temperature()
d.humidity()