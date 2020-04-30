
from application import app, db
from flask_login import login_required, current_user

from flask import redirect, render_template, request, url_for
from application.persons.forms import PersonForm
from application.persons.models import Person



@app.route("/persons", methods=["GET"])
def persons_index():
    return render_template("persons/list.html", persons = Person.query.all())

   

@app.route("/persons/new/")
def persons_form():
    return render_template("persons/new.html", form = PersonForm())


@app.route("/persons/", methods=["POST"])
def persons_create():
    form = PersonForm(request.form)
    if not form.validate():
        return render_template("persons/new.html", form = PersonForm)

    n = form.name.data
    b = form.dateOfBirth.data
    p = Person(n, b)
    p.account_id = 1
    db.session().add(p)
    db.session().commit()
    return redirect(url_for("persons_index"))

