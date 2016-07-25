from flask import Flask
import pipincontrol

app = Flask(__name__)

@app.route('/pin/<pin>/on')
def pin_high(pin):
    pipincontrol.set_pin_high(pin)

    return 'Pin ' + str(pin) + ' set to HIGH'

@app.route('/pin/<pin>/off')
def pin_low(pin):
    pipincontrol.set_pin_low(pin)

    return 'Pin ' + str(pin) + ' set to LOW'

@app.route('/pin/<pin>/status')
def pin_status(pin):
    pipincontrol.get_pin_status(pin)   
 
    return str(status)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
