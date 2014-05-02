import urllib2
import json
import numpy
from flask import Flask, render_template, request

app = Flask(__name__)      

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods= ['POST'])
def search():
    title = request.form['searchbar']
    movies = searchMovie(title)
    if movies != None:
        return render_template('search.html', movies=movies)
    else:
        msg=""
        return render_template('error.html', msg="No titles were found, please search again")

@app.route('/movieinfo', methods= ['POST'])
def movieInfo():
    imdbID = request.form['imdb']
    movie = getMovieInfo(imdbID)
    score = calcScore(movie)
    return render_template('movieinfo.html', movie=movie, score=score)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', msg="404, Page not found"), 404

def searchMovie(movieName):
    URL = "http://www.omdbapi.com/?s="    
    movieName = movieName.replace(" ", "%20")
    searchResults = json.load(urllib2.urlopen(URL+movieName))

    movies = []    
    try:
        for i in searchResults["Search"]:
            if i["Type"] == "movie":
                movies.append(i.copy())
    except KeyError:
        return None

    return movies

def getMovieInfo(imdbID):
    URL = "http://www.omdbapi.com/?i="
    movie = json.load(urllib2.urlopen(URL+str(imdbID)+"&tomatoes=true"))
    return movie

def calcScore(movie):
    scores = []
    try:
        scores.append(float(movie["Metascore"]))
    except:
        pass
    try:
        scores.append(float(movie["imdbRating"]) * 10)
    except:
        pass
    try:
        scores.append(float(movie["tomatoMeter"]))
    except:
        pass
    try:
        scores.append(float(movie["tomatoRating"]) * 10)
    except:
        pass
    try:
        scores.append(float(movie["tomatoUserMeter"]))
    except:
        pass
    try:
        scores.append(float(movie["tomatoUserRating"]) * 20)
    except:
        pass

    return int(round(numpy.mean(scores)))

if __name__ == '__main__':
    app.run(debug=True)