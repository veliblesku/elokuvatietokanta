from application import app, db
from flask import redirect, render_template, request, url_for
from application.users.models import User

@app.route("/users", methods=["GET"])
def users_index():
    return render_template("users/list.html", users = User.query.all())

@app.route("/users/new/")
def users_form():
    return render_template("users/new.html")

@app.route("/users/", methods=["POST"])
def users_create():
    n = request.form.get("name")
    p = request.form.get("password")
    u = User(n, p)
    db.session().add(u)
    db.session().commit()
    return redirect(url_for("users_index"))
