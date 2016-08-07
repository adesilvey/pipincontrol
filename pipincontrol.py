from time import sleep
import sys
import subprocess
import RPi.GPIO as GPIO

class PiPinControl:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)


    def set_pin_high(self, pin):
        try:
            pin = int(pin)

            GPIO.setup(pin, GPIO.OUT)

            sleep(0.2)
            GPIO.output(pin, GPIO.HIGH)
            sleep(0.2)
        except:
            e = sys.exc_func()[0]
            print "Exception error: ", e

    def set_pin_low(self, pin):
        try:
            pin = int(pin)

            GPIO.setup(pin, GPIO.OUT)

            sleep(0.2)
            GPIO.output(pin, GPIO.LOW)
            sleep(0.2)
        except:
            e = sys.exc_func()[0]
            print "Exception error: ", e

    def get_pin_status(self, pin):
        try:
            status = subprocess.check_output(['gpio', '-g', 'read', pin])
            
            return str(status)
        except:
            e = sys.exc_func()[0]
            print "Exception error: ", e
