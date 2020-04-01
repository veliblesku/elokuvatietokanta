from application import app, db
from flask_login import login_required, current_user

from flask import redirect, render_template, request, url_for
from application.movies.models import Movie
from application.ratings.models import Rating
from application.ratings.forms import MovieRatingForm

@app.route("/movies/<movie_id>/", methods=["POST"])
@login_required
def movie_set_rating(movie_id):
    form = MovieRatingForm(request.form)

    m = Movie.query.get(movie_id)
    u = current_user.id
    m.rating = form.rating.data
    r = Rating(form.rating.data)
    r.account_id = current_user.id
    r.movie_id = movie_id
    db.session.add(r)
    db.session().commit()
  
  
    return redirect(url_for("movies_get_movie", movie_id=movie_id))