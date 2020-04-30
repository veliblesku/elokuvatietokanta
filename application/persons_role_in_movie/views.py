from application import app, db
from flask_login import login_required, current_user

from flask import redirect, render_template, request, url_for
from application.persons_role_in_movie.models import PersonsRoleInMovie
from application.persons_role_in_movie.forms import PersonsRoleInMovieForm
from application.movies.models import Movie
from application.roles.models import Role
from application.persons.models import Person





@app.route("/add_credits", methods=["GET"])
def add_credits_index():
    form = PersonsRoleInMovieForm(request.form)
    return render_template("personsroleinmovie/personaddroleinmovie.html", movies = Movie.query.all(), roles = Role.query.all(), persons = Person.query.all(), form = form)

@app.route("/add_credits", methods=["POST"])
def add_credits():
    form = PersonsRoleInMovieForm(request.form)
    role = form.roles.data
    person = form.persons.data
    movie = form.movies.data
    s = PersonsRoleInMovie(movie=movie,role=role, person=person)
    db.session.add(s)
    db.session.commit()

    return redirect(url_for("add_credits_index"))

