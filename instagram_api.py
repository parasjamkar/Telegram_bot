import requests

ACCESS_TOKEN = "your_instagram_access_token"
BASE_URL = "https://graph.facebook.com/v16.0"

def fetch_instagram_emails():
    url = f"{BASE_URL}/me/accounts?access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    accounts = response.json().get('data', [])
    return [f"{account['name']}@example.com" for account in accounts]  # Mock emails
