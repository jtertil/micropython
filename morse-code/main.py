import machine
import time

LED_PIN = 2  # D4
BUTTON_PIN = 14  # D5
led = machine.Pin(LED_PIN, machine.Pin.OUT)
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

def dot():
    led.on()
    led.off()
    time.sleep(0.5)
    led.on()
    time.sleep(0.5)

def dash():
    led.on()
    led.off()
    time.sleep(1.5)
    led.on()
    time.sleep(0.5)

def space():
    led.on()
    time.sleep(1.5)

def space_w():
    led.on()
    time.sleep(3.5)


message = ['...', '---', '...']

led.on()

while True:
    for letter in message:
        for s in letter:
            if s == '.':
                dot()
            elif s == '-':
                dash()
        space()
    space_w()

