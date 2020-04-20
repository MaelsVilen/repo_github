from time import sleep
from itertools import cycle


class TrafficLight:
    __color = ['\033[91m' + 'red' + '\33[0m', '\33[33m' + 'yellow' + '\33[0m', '\33[32m' + 'green' + '\33[0m',
               '\33[33m' + 'yellow' + '\33[0m']

    def running(self):
        for el in cycle(self._TrafficLight__color):
            print('\r' + el, end='')
            if el == '\033[91m' + 'red' + '\33[0m':
                sleep(7)
            elif el == '\33[33m' + 'yellow' + '\33[0m':
                sleep(2)
            elif el == '\33[32m' + 'green' + '\33[0m':
                sleep(5)


tl = TrafficLight()
tl.running()
