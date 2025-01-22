from . import db

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.String, nullable=False)
    metric = db.Column(db.String, nullable=False)
    value = db.Column(db.Float, nullable=False)
