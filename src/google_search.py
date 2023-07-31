from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

from dotenv import dotenv_values

config = dotenv_values(".env")

GOOGLE_API_KEY = config["GOOGLE_API_KEY"]
GOOGLE_CSE_ID = config["GOOGLE_CSE_ID"]

search = GoogleSearchAPIWrapper(google_api_key=GOOGLE_API_KEY, google_cse_id=GOOGLE_CSE_ID, k=1)



tool = Tool(
    name="Google Search",
    description="Search Google and return a link.",
    func=search.run,
)

print(tool.run("provide me only the link for streaming the dark knight online in India specifically"))

