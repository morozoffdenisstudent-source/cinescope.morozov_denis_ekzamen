import requests

from conftest import test_movie_info
from custom_requester.custom_requester import CustomRequester
import pytest
import os
from dotenv import load_dotenv
from utils.data_generator import DataGenerator

load_dotenv()

class TestApiMoves:

    def test_get_movie_posters(self, api_manager):
        response = api_manager.movies_api.get_movie_posters()

        assert response.status_code == 200


    def test_create_movie(self, api_manager, authenticated_admin, test_movie_info):
        response = api_manager.movies_api.create_movie(test_movie_info)
        response_data = response.json()

        assert response.status_code == 201
        assert 'id' in response_data
        assert 'name' in response_data



    def test_get_movie_info(self, api_manager, created_movie):
        movie_id = created_movie['id']
        response = api_manager.movies_api.get_movie_info(movie_id)
        response_data = response.json()

        assert 'id' in response_data
        assert 'name' in response_data
        assert 'genreId' in response_data


    def test_delete_movie(self, api_manager, authenticated_admin, created_movie):
        movie_id = created_movie['id']
        response = api_manager.movies_api.delete_movie(movie_id)
        response_data = response.json()

        assert response.status_code == 200
        assert 'id' in response_data
        assert 'name' in response_data


    def test_update_movie(self, api_manager, created_movie, test_part_movie_info):
        movie_id = created_movie['id']
        old_movie_data = created_movie
        response = api_manager.movies_api.update_movie(movie_id, test_part_movie_info)
        response_data = response.json()

        assert response.status_code == 200
        assert response_data != old_movie_data


    def test_get_movie_posters_with_wrong_filters(self, api_manager):
        params = {"pageSize": DataGenerator.generate_random_negative_number(), "page": DataGenerator.generate_random_negative_number(), "locations": DataGenerator.generate_random_city()}
        response = api_manager.movies_api.get_movie_posters(expected_status=400, params=params)

        assert response.status_code == 400


    def test_create_movie_without_administrator_rights(self, api_manager, test_movie_info):
        response = api_manager.movies_api.create_movie(test_movie_info, expected_status=401)

        assert response.status_code == 401

    def test_create_duplicate_movie(self, api_manager, authenticated_admin, created_movie, test_movie_info):
        movie_name = created_movie['name']
        test_movie_info['name'] = movie_name

        response = api_manager.movies_api.create_movie(test_movie_info, expected_status=409)
        assert response.status_code == 409

    def test_get_not_existing_movie_info(self, api_manager, deleted_movie):
        movie_id = deleted_movie['id']
        response = api_manager.movies_api.get_movie_info(movie_id, expected_status=404)

        assert response.status_code == 404


    def test_delete_movie_without_administrator_rights(self, api_manager, created_movie):
        movie_id = created_movie['id']
        api_manager.auth_api.logout()
        response = api_manager.movies_api.delete_movie(movie_id, expected_status=401)

        assert response.status_code == 401


    def test_delete_not_existing_movie(self, api_manager, deleted_movie):
        movie_id = deleted_movie['id']
        response = api_manager.movies_api.delete_movie(movie_id, expected_status=404)

        assert response.status_code == 404


    def test_update_movie_without_administrator_rights(self, api_manager, created_movie, test_part_movie_info):
        movie_id = created_movie['id']
        api_manager.auth_api.logout()
        response = api_manager.movies_api.update_movie(movie_id, test_part_movie_info, expected_status=401)

        assert response.status_code == 401


    def test_update_not_existing_movie(self, api_manager, deleted_movie, test_part_movie_info):
        movie_id = deleted_movie['id']
        response = api_manager.movies_api.update_movie(movie_id, test_part_movie_info, expected_status=404)

        assert response.status_code == 404

















