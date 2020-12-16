import requests
from constants import API_URL, KEY


def get_movie_by_id(movie_id, language, append_to_response):
    url = f"{API_URL}/movie/{movie_id}{KEY}"
    params = {}
    if movie_id is not None:
        params["movie_id"] = movie_id

    if language is not None:
        params["language"] = language

    if append_to_response is not None:
        params["append_to_response"] = append_to_response

    return requests.get(url=url, params=params)


def post_movie_rating(movie_id, rate, guest_session_id):
    url = f"{API_URL}/movie/{movie_id}/rating{KEY}"
    params = {}
    if guest_session_id is not None:
        params["guest_session_id"] = guest_session_id

    return requests.post(url=url, params=params, json=rate)


def delete_movie_rating(movie_id, guest_session_id):
    url = f"{API_URL}/movie/{movie_id}/rating{KEY}"
    params = {}
    if guest_session_id is not None:
        params["guest_session_id"] = guest_session_id

    return requests.delete(url=url, params=params)
