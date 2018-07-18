

import random


# Fake DTH sensor library see
# 


class DHT:
    def __init__(self):
        print('Fake temperature sensor running')
        pass


def read_retry(sensor, pin):
    return (-1,-1)


DHT11 = DHT()
