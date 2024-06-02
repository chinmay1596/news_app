import requests
import os

from datetime import datetime

def fetch_news(keyword, from_date=None):
    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={os.getenv("NEWS_API_KEY")}'
    if from_date:
        url += f'&from={from_date.isoformat()}'
    response = requests.get(url)
    return response.json().get('articles', [])
