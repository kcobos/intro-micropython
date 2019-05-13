from machine import Pin, PWM
pwm0 = PWM(Pin(2))
pwm0.freq() # 0 - 1000
pwm0.freq(1000)
pwm0.duty() # 0 - 1023
pwm0.duty(200)
pwm0.deinit()
pwm1 = PWM(Pin(2), freq=500, duty=512)