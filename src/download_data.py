from pathlib import Path
import os
import requests

import sys

# from config.config import RAW_DATA_DIR

RAW_DATA_DIR = Path(__file__).parent.parent.absolute() / "data" / "raw"

movies_url = "https://datasets.imdbws.com/title.basics.tsv.gz"
ratings_url = "https://datasets.imdbws.com/title.ratings.tsv.gz"


with open(RAW_DATA_DIR / "title.basics.tsv.gz", "wb") as f:
    print(f"Downloading {movies_url}...")
    response = requests.get(movies_url)
    print(f"Writing to {f.name}...")
    f.write(response.content)
    print("Done.")



