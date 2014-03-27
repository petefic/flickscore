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
    return render_template('search.html', movies=movies)
 
@app.route('/movieinfo')
def movieInfo():
    return render_template('movieinfo.html')

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

if __name__ == '__main__':
    app.run(debug=True)