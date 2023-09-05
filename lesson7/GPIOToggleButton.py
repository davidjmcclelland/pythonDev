import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BOARD)

inPin = 40
outPin = 38
delay=.1
LEDstate = False
prevButtonState = False

gpio.setup(inPin,gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(outPin, gpio.OUT)
#switch the buttonState values in if statements
# to change from buttonUp to buttonDown
try:
    while True:
        buttonState = gpio.input(inPin)
        if buttonState == 1:
            LEDstate = not prevButtonState
        if buttonState == 0:
            prevButtonState = LEDstate
        gpio.output(outPin, LEDstate)
        print(buttonState)
        sleep(delay)
except KeyboardInterrupt:
    gpio.cleanup()
