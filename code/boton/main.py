import machine
boton = machine.Pin(4, machine.Pin.IN)
boton.value()
def boton_irq(p):
    print("El botón ha sido pulsado")
boton.irq(trigger=machine.Pin.IRQ_RISING, handler=boton_irq)
#boton.irq(trigger=machine.Pin.IRQ_FALLING, handler=boton_irq)