"""Forms for adopt app."""

from ast import Str
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField


class AddPetForm(FlaskForm):

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = StringField("Age")
    notes = StringField("Notes")
