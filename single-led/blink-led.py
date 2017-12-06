try:
    import RPi.GPIO as GPIO
except:
    from fakeGPIO import GPIO
import time


def main():
    # Establecemos el sistema de numeracion de pines
    GPIO.setmode(GPIO.BCM)
    # ponemos el gpio 18 como salida
    GPIO.setup(18, GPIO.OUT) 
    print('iniciando parpadeo')
    for i in range(60):
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.5)
    print('fin parpadeo')
    GPIO.cleanup()


if __name__ == '__main__':
    main()