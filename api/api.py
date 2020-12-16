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


def get_movie_by_id(movie_id):
    url = f"{API_URL}/movie/{movie_id}{KEY}"
    response = _request("get", url)
    return response


def get_movie_popular_list(language, page, region):
    url = f"{API_URL}/movie/popular{KEY}"
    params = {}
    if language is not None:
        params["language"] = language

    if page is not None:
        params["page"] = page

    if region is not None:
        params["region"] = region

    r = _request("get", url, query=params)
    return r


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
