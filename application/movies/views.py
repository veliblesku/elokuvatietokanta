
from application import app, db
from flask_login import login_required, current_user

from flask import redirect, render_template, request, url_for
from application.movies.models import Movie
from application.movies.forms import MovieForm
from application.ratings.models import Rating
from application.roles.models import Role
from application.persons.models import Person
from application.persons_role_in_movie.forms import PersonsRoleInThisMovieForm
from application.persons_role_in_movie.models import PersonsRoleInMovie



@app.route("/movies", methods=["GET"])
def movies_index():
    return render_template("movies/list.html", movies = Movie.query.all())

@app.route("/movies/<movie_id>/", methods=["GET"])
def movies_get_movie(movie_id):
    m = Movie.query.get(movie_id)
    r = Rating.find_movie_avg(movie_id)
    r_count = Rating.get_count_of_ratings_in_movie(movie_id)
    credits = PersonsRoleInMovie.get_credits(movie_id)    
    if r == None:
        return render_template("movies/movie.html",movie = m, form = MovieForm(), rating=r, rating_count = r_count, credits = credits)
    else:
        r = round(r,2)
        return render_template("movies/movie.html",movie = m, form = MovieForm(), rating=r, rating_count = r_count, credits = credits)


   

@app.route("/movies/new/")
@login_required
def movies_form():
    form = MovieForm(request.form)
    return render_template("movies/new.html", form = MovieForm())


@app.route("/movies/", methods=["POST"])
@login_required
def movies_create():
    form = MovieForm(request.form)
    if not form.validate():
        return render_template("movies/new.html", form = form)

    n = form.name.data
    d = form.duration.data
    b = form.budget.data
    y = form.year.data
    m = Movie(n, d, b,y)
    m.account_id = current_user.id
    db.session().add(m)
    db.session().commit()
    return redirect(url_for("movies_index"))


@app.route("/movies/<movie_id>/add_credits/", methods=["GET"])
def movie_add_credits_index(movie_id):
    form = PersonsRoleInThisMovieForm(request.form)
    movie = Movie.query.get(movie_id)
    return render_template("movies/movieaddcredits.html", movie = movie, roles = Role.query.all(), persons = Person.query.all(), form = form)

@app.route("/movies/<movie_id>/add_credits/", methods=["POST"])
def movie_add_credits(movie_id):
    form = PersonsRoleInThisMovieForm(request.form)
    role = form.roles.data
    person = form.persons.data
    movie = Movie.query.get(movie_id)
    s = PersonsRoleInMovie(movie=movie,role=role, person=person)
    db.session.add(s)
    db.session.commit()
    return redirect(url_for("movie_add_credits_index", movie_id = movie_id))

@app.route("/movies/<movie_id>/update/", methods=["GET"])
def movie_update_index(movie_id):
    m = Movie.query.get(movie_id)
    form = MovieForm(request.form)
    form.name.data = m.name
    form.budget.data = m.budget
    form.duration.data = m.duration
    form.year.data = m.year
    return render_template("movies/edit.html", movie = m, form = form)


@app.route("/movies/<movie_id>/update/", methods=["POST"])
def movie_update(movie_id):
    m = Movie.query.get(movie_id)
    form = MovieForm(request.form)
    m.name = form.name.data
    m.budget = form.budget.data
    m.year = form.year.data
    m.duration = form.duration.data
    db.session().commit()
    return redirect(url_for("movies_get_movie", movie_id = m.id))

@app.route("/movies/<movie_id>/delete/", methods=["POST"])
def movie_delete(movie_id):
    m = Movie.query.get(movie_id)
    Rating.query.filter(Rating.movie_id == movie_id).delete()
    db.session().delete(m)
    db.session().commit()
    return redirect(url_for("movies_index"))

@app.route("/movies/<movie_id>/delete_credit/<credit_id>", methods=["POST"])
def movie_delete_credit(movie_id, credit_id):
    c = PersonsRoleInMovie.query.get(credit_id)
    db.session().delete(c)
    db.session().commit()
    return redirect(url_for("movies_get_movie", movie_id = movie_id))