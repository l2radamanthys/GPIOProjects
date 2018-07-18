try:
    import RPi.GPIO as GPIO
except:
    from fakeGPIO import GPIO

try:
    import Adafruit_DHT
except:
    import fakeAdafruit_DHT as Adafruit_DHT

import GPIOshutils as sgpio
import time


# Puertos GPI LEDS
GREEN = 18
YELLOW = 16
RED = 20
BLUE = 12
SENSOR = 23



def main():
    sgpio.mode_bcm()
    sgpio.set_out(GREEN)
    sgpio.set_out(RED)
    sgpio.set_out(YELLOW)
    sgpio.set_out(BLUE)
    #animate_led(GREEN)
    #animate_led(YELLOW)
    #animate_led(RED)
    carrousel_led()
    sgpio.reset()


def toggle_led(port):
    sgpio.out_on(port)
    time.sleep(0.2)
    sgpio.out_off(port)
    time.sleep(0.1)



def animate_led(port):
    print('run', port)
    for i in range(5):
        toggle_led(port)



def carrousel_led():
    for i in range(20):
        toggle_led(GREEN)
        toggle_led(YELLOW)
        toggle_led(RED)
        toggle_led(BLUE)



if __name__ == '__main__':
    main()




