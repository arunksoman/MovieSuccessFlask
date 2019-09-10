from flask import Flask, render_template, request
import csv
import pandas as pd
from imdb import IMDb



ia = IMDb()
app = Flask(__name__)

app.secret_key='12345456778'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/movieCheck", methods=['POST', 'GET'])
def movieCheck():
    if not request.form.get("txtfilm"):
        return render_template("failure.html")
    # with open("registered.csv", "a") as file:
    search_for = request.form.get("txtfilm")
    movies = ia.search_movie(search_for)
    movieID = movies[0].movieID
    movie = ia.get_movie(movieID)
    actors = movie['cast']
    actor1 = actors[0]
    actor2 = actors[1]
    actor3 = actors[2]
    with open("registered.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["movie_name", "actor1","actor2","actor3"])
        if csv.Sniffer.has_header:
            writer.writeheader()
            writer.writerow({"movie_name": search_for, "actor1": actor1, "actor2": actor2, "actor3": actor3})
        writer.writerow({"movie_name": search_for, "actor1": actor1, "actor2": actor2, "actor3": actor3})
    return render_template("success.html")
