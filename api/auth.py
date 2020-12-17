import requests
from constants import API_URL, KEY, GUEST_SESSION


def get_guest_session_id(api_key=KEY):
    url = f"{API_URL}{GUEST_SESSION}new{api_key}"
    response = requests.get(url)
    return response.json()
