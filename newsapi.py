import requests

# Set your API key from newsapi.org
api_key = "0fad3152fa5746698931d1bb504f562b"

# Make a request to the News API
response = requests.get(
    f"https://newsapi.org/v2/top-headlines?country=in&apiKey=0fad3152fa5746698931d1bb504f562b"
)

# Convert the response to JSON format
articles = response.json()["articles"]

# Print the titles of the top 10 articles
for article in articles[:10]:
    print(article["title"])
