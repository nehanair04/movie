import pandas as pd
import datetime

movies={'title':['Avatar','Ratatouille','Pirates of the Caribbean: At World\'s End','Titanic',"The Hunger Games"],\
        'release date':['10-12-2009','22-06-2007','19-05-2007','18-11-1997','12-03-2012'],\
        'genre':[['Action','Adventure','Fantasy','Science Fiction'],['Animation','Comedy','Family','Fantasy'],["Adventure","Fantasy","Action"],["Drama","Romance","Thriller"],["Science Fiction","Adventure",]], \
        'rating':[7.2,7.5,6.9,7.5],'vote_count':[11800,4369,4500,7562]}


df = pd.DataFrame(movies)

import json

def suggest_movie(genres, ratings):
    with open('movies.json', 'r') as f:
        movies = json.load(f)
    
    # Filter the list of movies by genre and rating
    filtered_movies = [movie for movie in movies if movie['genre'] in genres and movie['rating'] in ratings]
    
    # Return a random movie from the filtered list
    import random
    return random.choice(filtered_movies)

# Test the suggest_movie function
print(suggest_movie(['action', 'comedy'], [8, 9, 10]))
