import machine
import time

LED_PIN = 2  # D4
BUTTON_PIN = 14  # D5
led = machine.Pin(LED_PIN, machine.Pin.OUT)
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

def switch():
    while True:
        if button.value() == 0:
            if led.value() == 1:
                led.off()
                time.sleep(0.5)
            elif led.value() == 0:
                led.on()
                time.sleep(0.5)

switch()
    
