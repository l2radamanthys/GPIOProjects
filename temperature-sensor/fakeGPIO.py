from random import randint


# Fake GPIO
__author__ = 'Ricardo D. Quiroga'
__version__ = '0.0.1'


class _GPIO:
    # modes
    BCM = 'BCM'
    BOARD = 'BOARD'

    OUT = 0
    IN = 1

    LOW = 0
    HIGH = 1


    def __init__(self):
        self.mode = None
        print('Fake GPIO running')


    def setmode(self, mode):
        self.mode = mode
        # print('SET MODE', mode)


    def setup(self, pin, mode):
        print('SET PIN MODE:', pin, mode)
        pass


    def input(self, pin):
        return randint(0,1)


    def output(self, pin, value):
        print('SET PIN:', pin, value)


    def cleanup(self, a=None):
        print('clear config')


GPIO = _GPIO()


