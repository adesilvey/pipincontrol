from time import sleep
import subprocess

from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

@app.route('/light/<pin>/on')
def light_on(pin):
    pin = int(pin)

    GPIO.setup(pin, GPIO.OUT)

    sleep(0.2)
    GPIO.output(pin, GPIO.HIGH)
    sleep(0.2)

    return 'Light on pin ' + str(pin) + ' turned on'

@app.route('/light/<pin>/off')
def light_off(pin):
    pin = int(pin)

    GPIO.setup(pin, GPIO.OUT)

    sleep(0.2)
    GPIO.output(pin, GPIO.LOW)
    sleep(0.2)

    return 'Light on pin ' + str(pin) + ' turned off'

@app.route('/light/<pin>/status')
def light_status(pin):
    status = subprocess.check_output(['gpio', '-g', 'read', pin])
    
    return str(status)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
