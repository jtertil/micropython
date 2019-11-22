import network
import machine
import dht

import urequests
import time

# config
LED_PIN = 2  # D4
led = machine.Pin(LED_PIN, machine.Pin.OUT)

DHT22_PIN = 4  # D2
sensor = dht.DHT22(machine.Pin(DHT22_PIN))

WLAN_SSID = ''
WLAN_PASSW = ''

API_KEY = ''
API_URL = 'https://api.thingspeak.com/update?api_key=' \
          '{API_KEY}&' \
          'field1={temperature}&' \
          'field2={humidity}'


def wifi_connect():
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    wifi = network.WLAN(network.STA_IF)

    if not wifi.isconnected():
        wifi.active(True)
        wifi.connect(WLAN_SSID, WLAN_PASSW)

        while not wifi.isconnected():
            time.sleep(5)
        print(wifi.ifconfig())


def read():
    led.off()
    sensor.measure()
    led.on()
    return sensor.temperature(), sensor.humidity()


def log_data(temperature, humidity):
    url = API_URL.format(
        API_KEY=API_KEY,
        temperature=temperature,
        humidity=humidity)

    response = urequests.get(url)
    print(response.status_code)


def run():
    while True:
        wifi_connect()
        t,h = read()
        log_data(t,h)
        time.sleep(300)


run()
