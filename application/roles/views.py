
from application import app, db
from flask_login import login_required, current_user

from flask import redirect, render_template, request, url_for
from application.roles.models import Role
from application.roles.forms import RoleForm
from application.roles.models import Role
from application.persons.models import Person

from application.movies.models import Movie



@app.route("/roles", methods=["GET"])
def roles_index():
    return render_template("roles/list.html", roles = Role.query.all())

@app.route("/roles/new/")
def roles_form():
    return render_template("roles/new.html", form = RoleForm())

@app.route("/roles/", methods=["POST"])
@login_required
def roles_create():
    form = RoleForm(request.form)
    if not form.validate():
        return render_template("roles/new.html", form = RoleForm)

    n = form.roleName.data
    r = Role(n)
    r.account_id = current_user.id
    db.session().add(r)
    db.session().commit()
    return redirect(url_for("roles_index"))


