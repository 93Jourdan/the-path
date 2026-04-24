# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    bio = db.Column(db.String(300), nullable=True)
    display_name = db.Column(db.String(80), nullable=True)
    avatar_url = db.Column(db.String(500), nullable=True)


    # Relationships
    sobriety = db.relationship('SobrietyTracker', backref='user', lazy=True)
    checkins = db.relationship('CheckIn', backref='user', lazy=True)
    spiritual_logs = db.relationship('SpiritualLog', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
    

class SobrietyTracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    addiction_type = db.Column(db.String(100), nullable=False)  # e.g. "Alcohol", "Gambling"
    start_date = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<SobrietyTracker {self.addiction_type}>'


class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mood = db.Column(db.String(50), nullable=False)       # e.g. "Hopeful", "Struggling"
    reflection = db.Column(db.Text, nullable=True)        # Optional journal entry
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<CheckIn {self.mood} {self.created_at}>'


class SpiritualLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    activity_type = db.Column(db.String(100), nullable=False)  # e.g. "Prayer", "Reading"
    note = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<SpiritualLog {self.activity_type}>'
    
class WallMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', foreign_keys=[author_id], backref='messages_sent')

    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref='wall_messages')

    def __repr__(self):
        return f'<WallMessage from {self.author_id} to {self.recipient_id}>'