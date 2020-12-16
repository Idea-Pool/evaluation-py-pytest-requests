from .base import TestBase
from api import auth
import pytest


_TOO_HIGH_VALUE_ERROR_MESSAGE = "Value too high: Value must be less than, or equal to 10.0."
_TOO_LOW_VALUE_ERROR_MESSAGE = "Value too low: Value must be greater than 0.0."


class TestPostMethod(TestBase):
    def setup_class(self):
        # Given the guest session id is retrieved
        session_response = auth.get_guest_session_id()
        self.id = session_response["guest_session_id"]

    def test_post_rating_message(self):
        # When the movie rating is sent
        response = self.post_movie_rating(
            status_code=201,
            movie_id="577922",
            guest_session_id=self.id,
            rate={"value": 9.0}
        )

        # Then the status_message should be "Success."
        assert (
                response["status_message"] == "Success."
        ), "The status message should indicate the successful rating"

    @pytest.mark.parametrize(
        "value, status_code, status_message",
        [
            (10.1, 400, _TOO_HIGH_VALUE_ERROR_MESSAGE),
            (10.1, 400, _TOO_HIGH_VALUE_ERROR_MESSAGE),
            (0.0, 400, _TOO_LOW_VALUE_ERROR_MESSAGE),
            (-6.5, 400, _TOO_LOW_VALUE_ERROR_MESSAGE),
        ]
    )
    def test_post_invalid_rating(self, value, status_code, status_message):
        # When the movie rating is sent
        response = self.post_movie_rating(
            status_code=status_code,
            movie_id="577922",
            guest_session_id=self.id,
            rate={"value": value}
        )
        assert (
                response["status_message"] == status_message
        ), f"The response should contain the '{status_message}' status message"
