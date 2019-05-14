try:
	import time as utime
except:
	import utime
try:
	import urequests as requests
except:
	import requests

def actualiza_ip(t):
	try:
		fip = open("ip","r")
		ip_old = fip.read()
		fip.close()
		domain = "esp8266.kcobos.es"
		res_ip = requests.get("http://ip.42.pl/raw")
		ip = res_ip.text
		ip = "1.1.1.2"
		if ip != ip_old:
			user = "usuario"
			password = "secreto"
			dir = "https://www.ovh.com/nic/update?system=dyndns&hostname="+domain+"&myip="+ip
			response = requests.get(dir, headers={'Authorization':""})
			fip = open("ip", "w")
			fip.write(ip)
			fip.close()
	except Exception as e:
		f = open("log", "a")
		f.write(str(utime.localtime()))
		f.write("  ERROR ACTUALIZA IP  ")
		f.write(str(e))
		f.write("\n")
		f.close()

