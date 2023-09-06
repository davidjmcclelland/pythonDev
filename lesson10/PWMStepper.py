import RPi.GPIO as gpio
from time import sleep

delay=.1
LEDpin = 37
brighterPin = 32
brighterButtonState = 1
brighterButtonStateOld = 0
dimmerPin = 36
dimmerButtonState = 1
dimmerButtonStateOld = 0
brightVal = 99

gpio.setmode(gpio.BOARD)
gpio.setup(LEDpin,gpio.OUT)
gpio.setup(brighterPin,gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(dimmerPin,gpio.IN, pull_up_down = gpio.PUD_UP)

pwm = gpio.PWM(LEDpin, 100)
pwm.start(brightVal)
try:
    while True:
        brighterButtonState = gpio.input(brighterPin)
        if brighterButtonStateOld == 0 and brighterButtonState == 1:
            brightVal = brightVal * 1.8
            print('brighten event')
        dimmerButtonState = gpio.input(dimmerPin)
        if dimmerButtonStateOld == 0 and dimmerButtonState == 1:
            brightVal = brightVal / 1.8
            print('dim event')
        if brightVal > 99:
            brightVal = 99
        if brightVal < 0:
            brightVal = 0
        # number in parens below is duty cycle vs off cycle
        pwm.ChangeDutyCycle(int(brightVal))
        brighterButtonStateOld = brighterButtonState
        dimmerButtonStateOld = dimmerButtonState
        sleep(delay)
except KeyboardInterrupt:
    pwm.stop()
    gpio.cleanup()
    print('GPIO good to go')