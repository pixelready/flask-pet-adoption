"""Flask app for adopt app."""

from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import FlaskForm

from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)

app.config["SECRET_KEY"] = "secret"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route("/", methods=["GET"])
def list_pets():
    """Homepage, lists all the pets"""

    pets = Pet.query.all()

    return render_template("pet_list.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def handle_new_pet_form():
    """Display new pet form, or handle submitted new pet data"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(
            name=name, species=species, photo_url=photo_url, age=age, notes=notes
        )

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added new pet: {name}, a {species}")
        return redirect("/")

    else:
        return render_template("new_pet_form.html", form=form)


@app.route("/<int:id>", methods=["GET"])
def show_pet_details(id):
    """Show the pet details"""

    pet = Pet.query.get_or_404(id)

    # TODO: add wtforms for edit form display

    return render_template("pet_details.html", pet=pet)
