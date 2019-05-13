import machine
led = machine.Pin(2, machine.Pin.OUT)
led.value()
led.off() # led.value(0)
led.on()  # led.value(1)