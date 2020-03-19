
from application import app, db
from flask import redirect, render_template, request, url_for
from application.movies.models import Movie

@app.route("/movies", methods=["GET"])
def movies_index():
    return render_template("movies/list.html", movies = Movie.query.all())

@app.route("/movies/new/")
def movies_form():
    return render_template("movies/new.html")

@app.route("/movies/", methods=["POST"])
def movies_create():
    n = request.form.get("name")
    d = request.form.get("duration")
    b = request.form.get("budget")
    m = Movie(n, d, b)
    db.session().add(m)
    db.session().commit()
    return redirect(url_for("movies_index"))

