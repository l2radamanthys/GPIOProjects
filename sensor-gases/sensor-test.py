try:
    import RPi.GPIO as GPIO
except:
    from fakeGPIO import GPIO
import time


port = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.IN)


try:
    while True:
        result = GPIO.input(port)
        if (result):
            print('Humo detectado', result)
        else:
            print('lectura', result)
        time.sleep(5)
except KeyboardInterrupt:
    print('close')
    GPIO.cleanup()

    
