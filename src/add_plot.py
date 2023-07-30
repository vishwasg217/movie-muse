from imdb import Cinemagoer, IMDbDataAccessError, IMDbError
import pandas as pd
import json

ia = Cinemagoer()

plots = {}

def get_movie_plot(movie_id):
    print("Getting plot for movie_id: {}".format(movie_id))
    movie = ia.get_movie(movie_id)
    return movie['plot'][0]

df = pd.read_csv('data/processed/pre_plot_data.csv')

movie_ids = df['tconst'].unique()

for i, movie_id in enumerate(movie_ids):
    print(f"Iter: {i} | Progress: {i/(len(movie_ids) - 1) * 100:.2f} | Movie ID: {movie_id}")

    try:
        plot = ia.get_movie(movie_id)['plot'][0]
    except (IMDbDataAccessError, IMDbError) as e:
        print(f"Error: {e}")
        plot = "N/A"
    
    movie_info = {str(movie_id): plot}

    plots.update(movie_info)

print(plots)

with open('data/processed/plot_data.json', 'w') as f:
    json.dump(plots, f)






