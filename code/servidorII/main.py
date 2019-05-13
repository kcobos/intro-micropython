import machine
led = machine.Pin(2, machine.Pin.OUT)
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(0)
while True:
   conn, addr = s.accept()
   print("Conexión desde: %s" % str(addr))
   request = conn.recv(512)
   request = str(request).split(" ")
   if request[1] == "/?LED=ON":
      led.on()
   if request[1] == "/?LED=OFF":
      led.off()
   print("Contenido recivido: %s" % str(request))
   conn.send("<html><head><title>Servidor ESP8266</title></head><body><h1>Hola desde mi IoT</h1><h2>%s</h2></body></html>"%led.value())
   conn.close()