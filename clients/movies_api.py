from custom_requester.custom_requester import CustomRequester
from config.base_urls import MOVIE_BASE_URL

MOVIES = '/movies'

class MoviesApi(CustomRequester):
    def __init__(self, session):
        super().__init__(session, base_url=MOVIE_BASE_URL)

    def get_movie_posters(self, expected_status=200, params=None, **kwargs):
        return self.send_request(
            method="GET",
            endpoint=f'{MOVIES}',
            expected_status=expected_status,
            params = params

        )

    def create_movie(self, movie_data, expected_status=201, **kwargs):
        return self.send_request(
            method="POST",
            endpoint=f'{MOVIES}',
            data=movie_data,
            expected_status= expected_status
        )

    def get_movie_info(self, movie_id, expected_status=200, **kwargs):
        return self.send_request(
            method="GET",
            endpoint=f'{MOVIES}/{movie_id}',
            expected_status= expected_status

        )

    def delete_movie(self, movie_id, expected_status=200, **kwargs):
        return self.send_request(
            method="DELETE",
            endpoint=f'{MOVIES}/{movie_id}',
            expected_status=expected_status

        )

    def update_movie(self, movie_id, movie_data, expected_status = 200, **kwargs):
        return self.send_request(
            method="PATCH",
            endpoint=f'{MOVIES}/{movie_id}',
            data=movie_data,
            expected_status=expected_status

        )




