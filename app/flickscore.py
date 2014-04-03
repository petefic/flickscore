import urllib2
import json
from flask import Flask, render_template, request
 
app = Flask(__name__)      
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods= ['POST'])
def search():
    title = request.form['searchbar']
    movies = searchMovie(title)
    return render_template('search.html', movies=movies)
 
@app.route('/movieinfo', methods= ['POST'])
def movieInfo():
    imdbID = request.form['imdb']
    movie = getMovieInfo(imdbID)
    return render_template('movieinfo.html', movie=movie)

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






if __name__ == '__main__':
    app.run(debug=True)
