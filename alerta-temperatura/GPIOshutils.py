try:
    import RPi.GPIO as GPIO
except:
    from fakeGPIO import GPIO


def mode_bcm():
    GPIO.setmode(GPIO.BCM)


def set_out(port):
    GPIO.setup(port, GPIO.OUT)


def set_in(port):
    GPIO.setup(port, GPIO.IN)


def out_on(port):
    GPIO.output(port, GPIO.HIGH)


def out_off(port):
    GPIO.output(port, GPIO.LOW)


def reset():
    GPIO.cleanup()