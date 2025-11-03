from datetime import datetime
from database import db


class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    cpu = db.Column(db.Float, nullable=False)
    memory = db.Column(db.Float, nullable=False)
    disk = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(16), default='Healthy', index=True)
    failure_type = db.Column(db.String(100), nullable=True)
    affected_app = db.Column(db.String(100), nullable=True)
    solution = db.Column(db.String(200), nullable=True)


class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    action = db.Column(db.String(32), nullable=False)
    result = db.Column(db.String(16), nullable=False)
    reward = db.Column(db.Float, nullable=False)
    recovery_time = db.Column(db.Float, nullable=True)  # seconds to recover
