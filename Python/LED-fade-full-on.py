
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
y = 0
inc = 50
pwm.set_pwm_freq(f)
print ("PWM frequency is {f}".format(f=f))
time.sleep(2)

print('DOING THANGS, press Ctrl-C to quit...')
while True:
    pwm.set_pwm(0, 0, x)
    print ("PWM 0 equals {x}".format(x=x))
    pwm.set_pwm(1, 0, 4095 - y) #invert this one to compare the two circuits
    print ("PWM 1 equals {y}".format(y=4095 - y))
    time.sleep(0.05)
