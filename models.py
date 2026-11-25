from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    game_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='waiting')

from datetime import datetime

class Move(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    card = db.Column(db.String(20))          # e.g. "AS", "KH", "10D"
    action = db.Column(db.String(50))        # e.g. "play", "draw", "discard"
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)