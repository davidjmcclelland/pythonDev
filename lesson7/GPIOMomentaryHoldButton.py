import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BOARD)

inPin = 40
outPin = 38
delay=.5
setVal = True;
gpio.setup(inPin,gpio.IN)
gpio.setup(outPin, gpio.OUT)
try:
    while True:
        readVal = gpio.input(inPin)
        if readVal == 1:
            setVal = not readVal
            gpio.output(outPin, setVal)
        if readVal == 0:
            setVal = not readVal
            gpio.output(outPin, setVal)
        print(readVal)
        sleep(delay)
except KeyboardInterrupt:
    gpio.cleanup()
