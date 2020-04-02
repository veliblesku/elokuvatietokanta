from application import app, db
from flask_login import login_required, current_user

from flask import redirect, render_template, request, url_for
from application.movies.models import Movie
from application.ratings.models import Rating
from application.ratings.forms import MovieRatingForm



@app.route("/myratings/", methods=["GET"])
@login_required
def ratings_get_user_ratings():
    u = current_user

    return render_template("ratings/user_ratings.html", ratings = Rating.find_movies_user_has_rated(u.id))

@app.route("/movies/<movie_id>/", methods=["POST"])
@login_required
def movie_set_rating(movie_id):
    form = MovieRatingForm(request.form)

    s = Rating.check_if_user_has_rated_movie(current_user.id,movie_id)
    if not s:
        print("empty")
        u = current_user.id
        r = Rating(form.rating.data)
        r.account_id = current_user.id
        r.movie_id = movie_id
        db.session.add(r)
        db.session().commit()
    else:
        r = Rating.query.get(s[0])
        r.rating = form.rating.data
        db.session().commit()
    print(s)


  
  
    return redirect(url_for("movies_get_movie", movie_id=movie_id))