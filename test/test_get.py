from .base import TestBase
import pytest


class TestGetMethod(TestBase):
    def test_get_status_code(self, movie_id, status_code):
        # When the movie data is retrieved
        response = self.get_movie_by_id(movie_id=movie_id)
        assert response.status_code == status_code

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
        assert response["title"] == title
