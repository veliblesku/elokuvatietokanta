
from application import app, db
from flask_login import login_required, current_user

from flask import redirect, render_template, request, url_for
from application.movies.models import Movie
from application.movies.forms import MovieForm

@app.route("/movies", methods=["GET"])
def movies_index():
    return render_template("movies/list.html", movies = Movie.query.all())

@app.route("/movies/new/")
@login_required
def movies_form():
    return render_template("movies/new.html", form = MovieForm())

@app.route("/movies/", methods=["POST"])
@login_required
def movies_create():
    form = MovieForm(request.form)
    if not form.validate():
        return render_template("movies/new.html", form = MovieForm)

    n = form.name.data
    d = form.duration.data
    b = form.budget.data
    m = Movie(n, d, b)
    m.account_id = current_user.id
    db.session().add(m)
    db.session().commit()
    return redirect(url_for("movies_index"))

