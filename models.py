"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.Text, default="", nullable=False)
    age = db.Column(
        db.Text,
        db.CheckConstraint('age in ["baby", "young", "adult", "senior"]'),
        nullable=False,
    )
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

