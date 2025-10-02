import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # Keep your key in environment

BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news(keyword=None, country="us", page_size=5):
    params = {
        "apiKey": NEWS_API_KEY,
        "pageSize": page_size,
    }
    if keyword:
        params["q"] = keyword
    else:
        params["country"] = country

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Error fetching news: {response.text}")

    data = response.json()
    return data.get("articles", [])
