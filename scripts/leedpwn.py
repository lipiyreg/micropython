#2/3/2023

from machine import Pin, PWM

pin = 7 #number for gpio pin

pwm_pin = PWM(Pin(pin))
#frequency is cycles per second (Hertz, Hz)
pwm_pin.freq(20) #Hz

percent = 10


pwm_pin.duty_u16(percent*655)