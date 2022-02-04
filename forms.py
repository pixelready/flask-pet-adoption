"""Forms for adopt app."""

from ast import Str
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, TextAreaField
from wtforms.validators import AnyOf, URL, Optional


class AddPetForm(FlaskForm):

    name = StringField("Pet Name")
    species = StringField("Species", validators=[AnyOf(["cat", "dog", "porcupine"])])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField(
        "Age",
        choices=[
            ("baby", "Baby"),
            ("young", "Young"),
            ("adult", "Adult"),
            ("senior", "Senior"),
        ],
        validators=[AnyOf(["baby", "young", "adult", "senior"])],
    )
    notes = TextAreaField("Notes")
