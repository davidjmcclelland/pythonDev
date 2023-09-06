import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
outPin = 37
gpio.setup(outPin,gpio.OUT)
# the 100 below refers to the pulse rate per second (HZ)
pwm = gpio.PWM(outPin, 100)


try:
    while True:
        #gpio.output(outPin, True)
        # number in parens below is duty cycle vs off cycle
        pwm.start(50)
except KeyboardInterrupt:
    gpio.cleanup()