import machine
import time

LED_PIN = 2  # D4
led = machine.Pin(LED_PIN, machine.Pin.OUT)

def blink():
    while True:
        time.sleep(0.5)
        led.on()
        time.sleep(0.5)
        led.off()

blink()
    
