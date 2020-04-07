from flask import render_template
from application import app

from flask_bootstrap import Bootstrap

Bootstrap(app)
@app.route("/")
def index():
    return render_template("index.html")
