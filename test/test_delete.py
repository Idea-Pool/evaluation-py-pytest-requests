from .base import TestBase
from api import auth


class TestDeleteMethod(TestBase):
    def setup_class(self):
        # Given the guest session id is retrieved
        session_response = auth.get_guest_session_id()
        self.id = session_response["guest_session_id"]

    def test_delete_movie_rating(self):
        # When the delete movie rating request is sent
        response = self.delete_movie_rating(movie_id="500", guest_session_id=self.id)
        assert (
                response.status_code == 200
        ), "The response should contain status code 200"

    def test_delete_movie_rating_message(self):
        # When the delete movie rating request is sent
        response = self.delete_movie_rating(status_code=200, movie_id="500", guest_session_id=self.id)
        assert (
                response["status_message"] == "The item/record was deleted successfully."
        ), "The status message should indicate the successful deletion"
