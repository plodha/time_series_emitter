from flask import Blueprint, jsonify, request
from .models import Event
from . import db

main = Blueprint('main', __name__)

# Stream Routes, this will get the information that is in the database
@main.route('/stream', methods=['GET'])
def stream():
    events = Event.query.order_by(Event.id.desc()).limit(10).all()
    data = [{"timestamp": e.timestamp, "metric": e.metric, "value": e.value} for e in events]
    return jsonify(data)

# This endponit will return the last N history of the events
@main.route('/history', methods=['GET'])
def history():
    n = request.args.get('n', default=5, type=int)
    events = Event.query.order_by(Event.id.desc()).limit(n).all()
    data = [{"timestamp": e.timestamp, "metric": e.metric, "value": e.value} for e in events]
    return jsonify(data)

# This endpoint will set the interval of the event emitter
# TODO: Work in Progress, currently this creates another thread and does not adjust the running thread. 
@main.route('/set_interval', methods=['POST'])
def set_interval():
    interval = request.json.get('interval', 2)
    return jsonify({"message": f"Interval set to {interval} seconds"})
