import RPi.GPIO as gpio
from time import sleep
delay=.1
rPin = 40
gPin = 38
bPin = 36
rSwitch = 37
gSwitch = 35
bSwitch = 33
rSwitchState = 0
gSwitchState = 0
bSwitchState = 0

gpio.setmode(gpio.BOARD)
gpio.setup(rPin,gpio.OUT)
gpio.setup(gPin,gpio.OUT)
gpio.setup(bPin,gpio.OUT)
gpio.setup(rSwitch,gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(gSwitch,gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(bSwitch,gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.output(rPin, 1)
gpio.output(gPin, 0)
gpio.output(bPin, 1)

try:
    while True:
        rSwitchState = gpio.input(rSwitch)
        gSwitchState = gpio.input(gSwitch)
        bSwitchState = gpio.input(bSwitch)
        print('gSwitchState: ' + str(gSwitchState))
        if rSwitchState == 0:
            gpio.output(rPin, 1)
            gpio.output(bPin, 0)
            gpio.output(gPin, 0)
        if gSwitchState == 0:
            gpio.output(rPin, 0)
            gpio.output(gPin, 1)
            gpio.output(bPin, 0)
        if bSwitchState == 0:
            gpio.output(rPin, 0)
            gpio.output(gPin, 0)
            gpio.output(bPin, 1)
        sleep(delay)
except KeyboardInterrupt:
    gpio.cleanup()
    print('GPIO good to go')