import urllib2
import json
import numpy

URL = "http://www.omdbapi.com/?"

#Search for a movie
searchResults = None
while searchResults is None:
    movieName = raw_input("Search for movie: ")
    movieName = movieName.replace(" ", "%20")
    
    searchResults = json.load(urllib2.urlopen(URL+"s="+movieName))

    movies = []
    try:
        for i in searchResults["Search"]:
            if i["Type"] == "movie":
                movies.append(i.copy())
    except KeyError:
        searchResults = None
        print "No movie found"
        
#Print search Results
count=0
for i in movies:
    count+=1
    print str(count) + ": " + i["Title"] + " (" + i["Year"] + ")"
    
#Pick a result
i = raw_input("Pick a movie: ")
selection = movies[int(i)-1].copy()

#Load the picked movie
title = selection["Title"]
title = title.replace(" ", "%20")
year = selection["Year"]
movie = json.load(urllib2.urlopen(URL+"t="+title+"&y="+year+"&tomatoes=true"))

#Add all the scores to a list
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

#Print avg score
print "The average rating is: " + str(int(round(numpy.mean(scores)))) + "/100"