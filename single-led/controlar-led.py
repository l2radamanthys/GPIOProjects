try:
    import RPi.GPIO as GPIO
except:
    from fakeGPIO import GPIO
import sys



def main():
    # Establecemos el sistema de numeracion de pines
    GPIO.setmode(GPIO.BCM)
    # ponemos el gpio 18 como salida
    GPIO.setup(18, GPIO.OUT) 

    if (len(sys.argv) == 2):
        mode = sys.argv[1]
        if mode == 'on':
            GPIO.output(18, GPIO.HIGH)

        elif mode == 'off':
            GPIO.output(18, GPIO.LOW)
            GPIO.cleanup()    

    else:
        print('error, debe pasar un parametro')
        GPIO.cleanup()



if __name__ == '__main__':
    main()




