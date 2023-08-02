import requests
from bs4 import BeautifulSoup

# URL of the IMDb page
url = "https://www.imdb.com/title/tt0468569/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Send a GET request to the URL
response = requests.get(url=url, headers=headers)
print(response)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Use BeautifulSoup to find the anchor tag with the specified data-testid attribute
    anchor_tag = soup.find('a', {'data-testid': 'tm-box-pwo-btn'})
    print(anchor_tag)
    # if anchor_tag:
    #     # Extract the value of the href attribute
    #     href_value = anchor_tag.get('href')
    #     print(f"The extracted href attribute value: {href_value}")
    # else:
    #     print("The specified element was not found on the page.")
else:
    print("Error: Unable to access the IMDb page.")
