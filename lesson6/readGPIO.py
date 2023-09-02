import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BOARD)

inPin = 40

gpio.setup(inPin,gpio.IN)
try:
    while True:
        readVal = gpio.input(inPin)
        print(readVal)
        sleep(.5)
except KeyboardInterrupt:
    gpio.cleanup()
