import requests
from constants import API_URL, KEY


def _request(method, url, query=None, body=None):
    if method == "get":
        return requests.get(url, params=query)
    elif method == "post":
        return requests.post(url, params=query, json=body)
    elif method == "put":
        return requests.put(url, params=query, json=body)
    elif method == "delete":
        return requests.delete(url, params=query)
    else:
        raise Exception(f"Not supported HTTP method: {method}")


def get_movie_by_id(movie_id, language, append_to_response):
    url = f"{API_URL}/movie/{movie_id}{KEY}"
    params = {}
    if movie_id is not None:
        params["movie_id"] = movie_id

    if language is not None:
        params["language"] = language

    if append_to_response is not None:
        params["append_to_response"] = append_to_response

    response = _request("get", url)
    return response


def post_movie_rating(movie_id, rate, guest_session_id):
    url = f"{API_URL}/movie/{movie_id}/rating{KEY}"
    params = {}
    if guest_session_id is not None:
        params["guest_session_id"] = guest_session_id

    r = _request("post", url, query=params, body=rate)
    return r


def delete_movie_rating(movie_id, guest_session_id):
    url = f"{API_URL}/movie/{movie_id}/rating{KEY}"
    params = {}
    if guest_session_id is not None:
        params["guest_session_id"] = guest_session_id

    r = _request("delete", url, query=params)
    return r
