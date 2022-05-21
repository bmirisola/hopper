from enum import Enum
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setmode(11, GPIO.OUT)

class LIGHT_SWITCH_STATES(Enum):
    OFF = 0
    ON = 1



def light_switch_operation(state):
    if(state == LIGHT_SWITCH_STATES.OFF):
        print('off')

    elif(state == LIGHT_SWITCH_STATES.ON):
        print('on')