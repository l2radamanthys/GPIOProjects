
try:
    import RPi.GPIO as GPIO
except:
    from fakeGPIO import GPIO

try:
    import Adafruit_DHT
except:
    import fakeAdafruit_DHT as Adafruit_DHT


def main():
    pin = 23 #usar el puerto GPIO23 para entrada
    sensor = Adafruit_DHT.DHT11
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, hum))


if __name__ == '__main__':
    main()