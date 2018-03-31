
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

f = 1000
x = 0
pwm.set_pwm_freq(f)
print ("PWM frequency is {f}".format(f=f))
time.sleep(2)

print('DOING THANGS, press Ctrl-C to quit...')
while True:
    pwm.set_pwm(0, 0, x)
    x = x + 25
    if x >= 4095:
        x = 0
    print ("PWM equals {x}".format(x=x))
    time.sleep(0.05)
