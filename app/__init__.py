from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register the routes
    from .routes import main
    app.register_blueprint(main)

    # Auto Initilize the database
    with app.app_context():
        db.create_all()

    # start the services
    from .services import start_event_emitter
    start_event_emitter(app, interval=2)

    return app
