import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.off()
    time.sleep(1)
    led.on()
    time.sleep(0.5)

