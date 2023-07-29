from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

movie = ia.get_movie("0068646")
print(movie['plot'][0])
print(movie['genres'])
print(movie['rating'])
print(movie['year'])

