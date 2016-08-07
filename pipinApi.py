from flask import Flask, jsonify, request, make_response
from pipincontrol import PiPinControl as ppc

app = Flask(__name__)

from werkzeug.debug import DebuggedApplication
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
app.debug = True

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({ 'error' : 'Not Found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({ 'error' : 'Bad request'}), 400)

@app.route('/', methods=['GET'])
def test():
    return make_response('Everything looks ok here', 200)

@app.route('/pin/<pin>/on', methods=['GET','POST'])
def pin_high(pin):
    ppc.set_pin_high(pin)

    return make_response(jsonify({ 'Message' : 'Pin ' + str(pin) + ' set to HIGH' }), 200)

@app.route('/pin/<pin>/off')
def pin_low(pin):
    ppc.set_pin_low(pin)

    return make_response(jsonify({ 'Message' : 'Pin ' + str(pin) + ' set to LOW' }), 200)

@app.route('/pin/<pin>/status', methods=['GET','POST'])
def pin_status(pin):
    status = ppc.get_pin_status(pin)   
 
    return make_response(jsonify({ 'Status' : status}), 200)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
