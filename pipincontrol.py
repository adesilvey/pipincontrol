from time import sleep
import subprocess

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def set_pin_high(pin):
    pin = int(pin)

    GPIO.setup(pin, GPIO.OUT)

    sleep(0.2)
    GPIO.output(pin, GPIO.HIGH)
    sleep(0.2)

def set_pin_low(pin):
    pin = int(pin)

    GPIO.setup(pin, GPIO.OUT)

    sleep(0.2)
    GPIO.output(pin, GPIO.LOW)
    sleep(0.2)

def get_pin_status(pin):
    status = subprocess.check_output(['gpio', '-g', 'read', pin])

    return str(status)
