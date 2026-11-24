import requests
from custom_requester.custom_requester import CustomRequester
import pytest



class TestAuth:
    def test_register_user(self, api_manager, test_user):
        response = api_manager.auth_api.register_user(test_user)
        response_data = response.json()

        assert response_data["email"] == test_user["email"]
        # добавим еше проверок
        assert "id" in response_data
        assert "USER" in response_data["roles"]

    def test_register_and_login_user(self, api_manager, registered_user):
        login_data = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        response = api_manager.auth_api.login_user(login_data)
        response_data = response.json()

        assert "accessToken" in response_data
        assert response_data["user"]["email"] == registered_user["email"]

    def test_get_user_info(self, api_manager, authenticated_user):
        response = api_manager.user_api.get_user_info(authenticated_user["id"])
        response_data = response.json()

        assert response_data["email"] == authenticated_user["email"]
        assert response_data['id'] == authenticated_user["id"]



    def test_delete_user(self, api_manager, authenticated_user):
        id = authenticated_user["id"]
        response = api_manager.user_api.delete_user(id)

        assert response.status_code == 200


    def test_logout_user(self, api_manager, authenticated_user):
        api_manager.auth_api.logout()
        id = authenticated_user["id"]

        assert 'authorization' not in api_manager.session.headers
        assert api_manager.user_api.delete_user(id, expected_status=401).status_code == 401






