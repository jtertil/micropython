import network
import machine
import dht

import urequests
import time
import setup

# config
led = machine.Pin(setup.LED_PIN, machine.Pin.OUT)
sensor = dht.DHT22(machine.Pin(setup.DHT22_PIN))



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


def run():
    while True:
        wifi_connect()
        t, h = read()
        log_data(t, h)
        time.sleep(setup.READ_INTERV * 60)


run()
