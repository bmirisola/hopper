import time
from enum import Enum

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50)
servo1.start(0)


class LIGHT_SWITCH_STATES(Enum):
    OFF = 0
    ON = 1


### https://www.youtube.com/watch?v=xHDT4CwjUQE
## Code stolen  from above link ^
def light_switch_operation(state):
    if (state == LIGHT_SWITCH_STATES.OFF):
        print('Turning light off')
        servo1.ChangeDutyCycle(12)  # Change this number
        time.sleep(.5)
        servo1.ChangeDutyCycle(0)
        time.sleep(.3)

    elif (state == LIGHT_SWITCH_STATES.ON):
        print('Turning light on')
        servo1.ChangeDutyCycle(2)  # Change this number
        time.sleep(1)
        servo1.ChangeDutyCycle(0)
        time.sleep(.3)


def lightswitch_function():
    servo1.ChangeDutyCycle(12)  # Change this number
    time.sleep(.8)
    servo1.ChangeDutyCycle(0)
    time.sleep(.1)
    servo1.ChangeDutyCycle(2)  # Change this number
    time.sleep(.8)
    servo1.ChangeDutyCycle(0)
    time.sleep(.5)
