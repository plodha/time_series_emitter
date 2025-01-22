import time
from datetime import datetime, timezone

# Generate events in the background.
def generate_events(app, interval, metric="temperature"):
    with app.app_context():
        from .models import Event
        from . import db

        while True:
            timestamp = datetime.now(timezone.utc).isoformat() + "Z"
            value = round(20 + 10 * (time.time() % 1), 2)
            new_event = Event(timestamp=timestamp, metric=metric, value=value)
            db.session.add(new_event)
            db.session.commit()
            time.sleep(interval)

# Start the event emitter in a separate thread.
def start_event_emitter(app, interval):
    import threading
    thread = threading.Thread(target=generate_events, args=(app, interval))
    thread.daemon = True
    thread.start()
