import webrepl
webrepl.start()

import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.isconnected()
wlan.connect('essid', 'password')
wlan.ifconfig()

# ap = network.WLAN(network.AP_IF)
# ap.active(True)
# ap.config(essid='ESP-AP', password='miESPap123')
# ap.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8'))