from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1"
IMG_PATH = "https://image.tmdb.org/t/p/w1280"
SEARCH_API = "https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query="


@app.route("/")
def index():
    # Initially get popular movies
    movies = get_movies(API_URL)
    return render_template("index.html", movies=movies)


@app.route("/search", methods=["POST"])
def search():
    if request.method == "POST":
        search_term = request.form["search"]
        if search_term:
            # Get movies based on the search term
            movies = get_movies(SEARCH_API + search_term)
            return render_template("index.html", movies=movies)
    return redirect("/")


def get_movies(url):
    resp = requests.get(url)
    resp_data = resp.json()
    return resp_data["results"]


def get_class_by_rate(vote):
    if vote >= 8:
        return "green"
    elif vote >= 5:
        return "orange"
    else:
        return "red"


if __name__ == "__main__":
    app.run(debug=True)
