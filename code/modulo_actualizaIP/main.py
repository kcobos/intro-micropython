import machine
import ntptime
import u_ip
ntptime.settime() #actualiza hora
tim = machine.Timer(-1)
u_ip.actualiza_ip(0) #actualiza ip al iniciar
tim.init(period=120000, mode=machine.Timer.PERIODIC, callback=u_ip.actualiza_ip) #actualiza ip cada 2 minutos