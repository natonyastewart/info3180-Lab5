# Add any model classes for Flask-SQLAlchemy here
from datetime import datetime 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.model):
    id = db.Column(db.integer, primary_key = True)
    title = db.Column(db.string)
    description = db.Column(db.string)
    poster = db.Column(db.string)
    created_at = db.Column(db.DateTime, default = datetime.now(timezone.utc))


def __repr__(self):
    return f"<Movie {self.title}>"