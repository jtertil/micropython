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

def err_blink(num):
    while True:
        for i in range(num):
            led.on()
            time.sleep(0.2)
            led.off()
            time.sleep(0.2)
        led.on()
        time.sleep(1)

MORSE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}

try:
    file = open('message.txt', 'r')
    message = file.readline().rstrip('\n')
except OSError:
    err_blink(5)

# message = 'HELLO WORLD'
morse = ''

for letter in message:
    if letter in MORSE_DICT:
        morse += MORSE_DICT[letter] + ' ' 
    elif letter == ' ':
        morse += '/'

led.on()

while True:
    for s in morse:
        if s == '.':
            dot()
        elif s == '-':
            dash()
        elif s == ' ':
            space()
        elif s == '/':
            space_w()

