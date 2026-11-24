import requests
import pytest
from clients.api_manager import ApiManager
from faker import Faker
import os
from dotenv import load_dotenv
import random
from utils.data_generator import DataGenerator

load_dotenv()

@pytest.fixture(scope="session")
def session():
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture(scope="session")
def api_manager(session):
    return ApiManager(session)


@pytest.fixture(scope="function")
def test_user():
    password = DataGenerator.generate_random_password()

    return {
        "email": DataGenerator.generate_random_email(),
        "fullName": DataGenerator.generate_random_name(),
        "password": password,
        "passwordRepeat": password,
        "roles": ["USER"]
    }


@pytest.fixture(scope="function")
def registered_user(api_manager, test_user):
    response = api_manager.auth_api.register_user(test_user).json()
    test_user["id"] = response["id"]
    return test_user


@pytest.fixture(scope="session")
def unauthenticated_api_manager(registered_user):
    session = requests.Session()
    yield ApiManager(session)
    session.close()


@pytest.fixture(scope="function")
def authenticated_user(api_manager, registered_user):
    api_manager.auth_api.authenticate((registered_user['email'], registered_user['password']))
    return registered_user


@pytest.fixture(scope="function")
def authenticated_admin(api_manager):
    api_manager.auth_api.authenticate((os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD")))
    response = api_manager.user_api.get_user_info(os.getenv("ADMIN_EMAIL"))

    return response.json

@pytest.fixture(scope="function")
def test_movie_info():

    return {
        'name': DataGenerator.generate_random_movie_name(),
        'imageUrl': DataGenerator.generate_random_img_url(),
        "price": DataGenerator.generate_random_price(),
        'description': DataGenerator.generate_random_description(),
        'location': DataGenerator.generate_random_location(),
        'published': True,
        'genreId': DataGenerator.generate_random_genre_id()

    }


@pytest.fixture(scope="function")
def created_movie(api_manager, test_movie_info):
    admin_email = os.getenv("ADMIN_EMAIL")
    admin_password = os.getenv("ADMIN_PASSWORD")

    api_manager.auth_api.authenticate((admin_email, admin_password))
    response = api_manager.movies_api.create_movie(test_movie_info)
    created_movie_info = response.json()

    return created_movie_info


@pytest.fixture(scope="function")
def deleted_movie(api_manager, created_movie):
    movie_id = created_movie['id']
    movie_data = created_movie
    api_manager.movies_api.delete_movie(movie_id)

    return movie_data


@pytest.fixture(scope="function")
def test_part_movie_info():
    return {
        'name': DataGenerator.generate_random_movie_name(),
        'imageUrl': DataGenerator.generate_random_img_url(),
        "price": DataGenerator.generate_random_price(),
        'description': DataGenerator.generate_random_description()


    }







