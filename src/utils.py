import pandas as pd
import json
from dotenv import dotenv_values

config = dotenv_values(".env")
OPEN_AI_API = config["OPEN_AI_API"]
ACTIVELOOP_TOKEN = config["ACTIVELOOP_TOKEN"]


def get_credentials():
    config = dotenv_values(".env")
    OPEN_AI_API = config["OPEN_AI_API"]
    ACTIVELOOP_TOKEN = config["ACTIVELOOP_TOKEN"]
    return OPEN_AI_API, ACTIVELOOP_TOKEN

def load_and_convert_to_json(path: str) -> json:
    """
    Load data from a given path and convert it to a list of json objects.
    """
    data = pd.read_csv(path)
    data = data.to_dict(orient="records")
    return data