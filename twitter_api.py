import requests

BEARER_TOKEN = "your_twitter_bearer_token"
BASE_URL = "https://api.twitter.com/2"

def fetch_twitter_emails():
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    query = "influencer email"
    url = f"{BASE_URL}/tweets/search/recent?query={query}"
    response = requests.get(url, headers=headers)
    tweets = response.json().get('data', [])
    return [f"{tweet['author_id']}@example.com" for tweet in tweets]  # Mock emails
