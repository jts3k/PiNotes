
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()


#pwm.set_pwm_freq(60)

numberOfLEDs = 16


print('DOING THANGS, press Ctrl-C to quit...')
while True:
    for x in range(0, numberOfLEDs):
        pwm.set_pwm(x, 0, 4095)
        pwm.set_pwm(x - 1, 0, 0)
        time.sleep(0.1)
