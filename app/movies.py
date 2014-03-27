import urllib2
import json
import numpy

URL = "http://www.omdbapi.com/?"

def searchMovie(movieName):

	movieName = movieName.replace(" ", "%20")
	searchResults = json.load(urllib2.urlopen(URL+"s="+movieName))
    
	movies = []
	
	try:
	    for i in searchResults["Search"]:
		if i["Type"] == "movie":
		    movies.append(i.copy())
	except KeyError:
	    return None
    
	return movies

def loadMovieInfo(selection, searchResults):
	movie = []
	return movie


