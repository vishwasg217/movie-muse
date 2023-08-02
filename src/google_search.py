from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

from dotenv import dotenv_values

config = dotenv_values(".env")

BING_SUBSCRIPTION_KEY = config["BING_SUBSCRIPTION_KEY"]
BING_SEARCH_URL = config["BING_SEARCH_URL"]

from langchain.utilities import BingSearchAPIWrapper

search = BingSearchAPIWrapper(bing_subscription_key=BING_SUBSCRIPTION_KEY, bing_search_url=BING_SEARCH_URL,k=1)

print(search.results("find me the link for streaming the movie the dark knight in India ", 5)[0])





