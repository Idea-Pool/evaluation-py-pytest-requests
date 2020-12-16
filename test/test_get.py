from .base import TestBase
import pytest
import sys


class TestGetMethod(TestBase):
    @pytest.mark.skipif(sys.version_info < (5, 7), reason="requires python 3.7 or higher")
    def test_get_status_code(self):
        # When the movie data is retrieved
        response = self.get_movie_by_id(movie_id="500")
        assert (
                response.status_code == 200
        ), "The response should contain status code 200"

    @pytest.mark.parametrize(
        "movie_id, title",
        [
            ("335983", "Venom"),
            ("577922", "Tenet"),
            ("420818", "The Lion king")
        ]
    )
    def test_get_response_title(self, movie_id, title):
        # When the movie data is retrieved
        response = self.get_movie_by_id(status_code=200, movie_id=movie_id)
        # Then the title should be equal to the title that belongs to the ID
        assert (
                response["title"] == title
        ), f"The '{movie_id}' ID should have the '{title}' title"
