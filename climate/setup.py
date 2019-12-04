pins = {'D0': 16, 'D1': 5, 'D2': 4, 'D3': 0, 'D4': 2,
        'D5': 14, 'D6': 12, 'D7': 13, 'D8': 15}


# config
LED_PIN = 2  # D4
DHT22_PIN = 4  # D2
I2C_SCL_PIN = 14  # D5
I2C_SDA_PIN = 12  # D6


WLAN_SSID = ''
WLAN_PASSW = ''

API_KEY = ''
API_URL = 'https://api.thingspeak.com/update?api_key=' \
          '{API_KEY}&' \
          'field1={temperature}&' \
          'field2={humidity}'

READ_INTERV = 5  # read interval in minutes
