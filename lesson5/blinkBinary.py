import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
LEDS = {  
    1:37,
    2:35,
    3:33,
    4:31,
    5:29
 }
bins = [
    [0,0,0,0,0],
    [0,0,0,0,1],
    [0,0,0,1,0],
    [0,0,0,1,1],
    [0,0,1,0,0],
    [0,0,1,0,1],
    [0,0,1,1,0],
    [0,0,1,1,1],
    [0,1,0,0,0],
    [0,1,0,0,1],
    [0,1,0,1,0],
    [0,1,0,1,1],
    [0,1,1,0,0],
    [0,1,1,0,1],
    [0,1,1,1,0],
    [0,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,1],
    [1,0,0,1,0],
    [1,0,0,1,1],
    [1,0,1,0,0],
    [1,0,1,0,1],
    [1,0,1,1,0],
    [1,0,1,1,1],
    [1,1,0,0,0],
    [1,1,0,0,1],
    [1,1,0,1,0],
    [1,1,0,1,1],
    [1,1,1,0,0],
    [1,1,1,0,1],
    [1,1,1,1,0],
    [1,1,1,1,1],
]
for LED in LEDS:
    #print('led: ' + str(LEDS[LED]))
    #print('led: ' + str(LED))
    #print('bin: ' + str(bins[LED]))
    gpio.setup(LEDS[LED], gpio.OUT)

for bin in bins:
    for i in range(len(bin)):
        for LED in LEDS:
            print('led: ' + str(LEDS[LED]))
            print('led pos: ' + str(LED))
            print('bin: ' + str(bin))
            print('bin i: ' + str(bin[i]))
            gpio.output(LEDS[i + 1],bin[i])
    time.sleep(1)
# for LED in LEDS:
#     gpio.output(LEDS[LED],False)
# time.sleep(.5)

gpio.cleanup()