import time
import network

import urequests
import setup

from machine import Pin, I2C
from dht import DHT22
from ssd1306 import SSD1306_I2C


led = Pin(setup.LED_PIN, Pin.OUT)
sensor = DHT22(Pin(setup.DHT22_PIN))
i2c = I2C(
    scl=Pin(setup.I2C_SCL_PIN),
    sda=Pin(setup.I2C_SDA_PIN))
i2c.scan()
display = SSD1306_I2C(128, 64, i2c)


def wifi_connect():
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    wifi = network.WLAN(network.STA_IF)

    while not wifi.isconnected():
        print('Connecting to {}'.format(setup.WLAN_SSID))
        wifi.active(True)
        wifi.connect(setup.WLAN_SSID, setup.WLAN_PASSW)
        time.sleep(5)

    print('Connected to {}'.format(setup.WLAN_SSID))
    print('Network config: {}'.format(wifi.ifconfig()))


def read():
    led.off()
    sensor.measure()
    led.on()
    return sensor.temperature(), sensor.humidity()


def log_data(temperature, humidity):
    url = setup.API_URL.format(
        API_KEY=setup.API_KEY,
        temperature=temperature,
        humidity=humidity)
    try:
        response = urequests.get(url)
        print('Response code: ', response.status_code)
    except Exception as err:
        print('Request error: ', err)


def display_data(temperature, humidity):
    display.fill(0)
    display.text('temp.: {} C'.format(temperature), 0, 0)
    display.text('humidity: {} %'.format(humidity), 0, 32)
    display.show()


def run():
    while True:
        wifi_connect()
        t, h = read()
        display_data(t, h)
        log_data(t, h)
        time.sleep(setup.READ_INTERV * 60)


run()
