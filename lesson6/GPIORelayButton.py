import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BOARD)

inPin = 40
outPin = 38
delay=.5

gpio.setup(inPin,gpio.IN)
gpio.setup(outPin, gpio.OUT)
try:
    while True:
        readVal = gpio.input(inPin)
        if readVal == 1:
            gpio.output(outPin, 1)
        if readVal == 0:
            gpio.output(outPin, 0)
        print(readVal)
        sleep(delay)
except KeyboardInterrupt:
    gpio.cleanup()
