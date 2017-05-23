from flask import Flask, jsonify
from Parking import Parking
from  Car import Car
from  Parser import ParserInput
app = Flask(__name__)
#https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

cars = []
events_example = '{"eventId": {"car": {"carId": "1","dataOut": "2017-04-22 17:13:25","owner": "tata"},"dataNow": "2017-04-22 14:15:25","typ": "in"},"eventId2": {"car": {"carId": "1","dataIn": "2017-04-22 14:13:25","owner": "tata"},"dataNow": "2017-04-22 11:13:25","typ": "out"},"eventId3": {"car": {"carId": "1","dataIn": "2017-04-22 14:13:25","owner": "tata"},"dataNow": "2017-04-22 13:13:25","typ": "out"}}'
parkings = []



@app.route('/parking_state/<int:park_id>', methods=['GET'])
def get_state(park_id):
    try:
        park = parkings[park_id]
    except:
        abort(404)
    return jsonify({'parking': park.printMe()})

@app.route('/parking_status/<int:park_id>', methods=['GET'])
def get_status(park_id):
    try:
        park = parkings[park_id]
    except:
        abort(404)
    return jsonify({'parking': park.getParkingStatus()})



from flask import request,abort

@app.route('/new_parking', methods=['POST'])
def new_parking():
    if not request.json or not 'x' in request.json or not 'y' in request.json:
        abort(400)
    p = Parking(request.json['x'], request.json['y'])
    parkings.append(p)
    id = parkings.index(p)
    return jsonify({'parking': parkings[id].printMe(), 'id':id}), 201


@app.route('/give_events', methods=['POST'])
def events():
    if not request.json:
        abort(400)
    events = ParserInput(request.json)
    try:
        events.parseMyLines()
    except:
        abort(400)
    cars = events.manageCars()
    return jsonify({'parking': parkings[id].printMe(), 'id':id}), 201

@app.route('/give_next_time_event', methods=['GET'])
def it_is_event_time():
    return jsonify({'event': events.getNextEvent()}), 201

@app.route('/do_next_event', methods=['GET'])
def do_event():
    type,event=events.doNextEvent()
    car = [c for c in cars if c.getCarId() == event[1]['car']['carId']][0]
    if type:
        path = parkings[0].parkCar(car)
    else:
        path = parkings[0].takeCar(car)
    return jsonify({'event': path,'parking': parkings[0].printMe()}), 201


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
