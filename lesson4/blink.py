import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)
numBlink = int(input('How many blinks? '))
for i in range(0, numBlink):
    gpio.output(11,True)
    time.sleep(1)
    gpio.output(11,False)
    time.sleep(.5)
gpio.cleanup()