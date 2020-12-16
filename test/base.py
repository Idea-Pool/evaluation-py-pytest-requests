from api.api import get_movie_by_id, get_movie_popular_list, post_movie_rating, delete_movie_rating


class TestBase:
    def get_movie_by_id(self, status_code=None, movie_id=False):
        response_get = get_movie_by_id(movie_id)
        if not status_code is None:
            assert (
                    response_get.status_code == status_code
            ), f"response's status code is {response_get.status_code}, it should be {status_code}"
            return response_get.json()
        return response_get

    def get_movie_popular_list(self, status_code=None, language=None, page=None, region=None):
        if language is False:
            language = self.language
        if page is False:
            page = self.page
        if region is False:
            region = self.region
        response_get = get_movie_popular_list(
            language=language,
            page=page,
            region=region
        )
        if not status_code is None:
            assert (
                    response_get.status_code == status_code
            ), f"response's status code is {response_get.status_code}, it should be {status_code}"
        return response_get.json()

    def post_movie_rating(self, status_code=None, movie_id=None, guest_session_id=None, rate=None):
        if movie_id is False:
            movie_id = self.movie_id
        if guest_session_id is False:
            guest_session_id = self.guest_session_id
        response_post = post_movie_rating(
            movie_id=movie_id,
            guest_session_id=guest_session_id,
            rate=rate
        )
        if not status_code is None:
            assert (
                    response_post.status_code == status_code
            ), f"response's status code is {response_post.status_code}, it should be {status_code}"
        return response_post.json()

    def delete_movie_rating(self, status_code=None, movie_id=None, guest_session_id=None):
        if movie_id is False:
            movie_id = self.movie_id
        if guest_session_id is False:
            guest_session_id = self.guest_session_id
        response_delete = delete_movie_rating(
            movie_id=movie_id,
            guest_session_id=guest_session_id
        )
        if not status_code is None:
            assert (
                    response_delete.status_code == status_code
            ), f"response's status code is {response_delete.status_code}, it should be {status_code}"
            return response_delete.json()
        return response_delete
