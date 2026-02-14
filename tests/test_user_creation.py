import allure
from generators import *
from methods.user_methods import UserMethods


class TestUserCreation:

    @allure.title("Тестируем, что пользователь успешно создаётся")
    def test_user_creation_success(self, user_creation):
        credentials = user_creation
        response = UserMethods.user_creation(credentials)
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "accessToken" in response.json()
    
    @allure.title("Тестируем, что нельзя создать двух одинаковых пользователей")
    def test_user_creation_with_same_credentials_not_possible(self, user_creation):
        credentials = user_creation
        response = UserMethods.user_creation(credentials)
        response = UserMethods.user_creation(credentials)
        assert response.status_code == 403
        assert response.json()["success"] == False
        assert response.json()["message"] == "User already exists"

    @allure.title("Тестируем, что создание пользователя с пустым полем email возвращает ошибку")
    def test_user_creation_without_email_return_error(self, user_creation):
        credentials = user_creation
        credentials["email"] = ""
        response = UserMethods.user_creation(credentials)
        assert response.status_code == 403
        assert response.json()["success"] == False
        assert response.json()["message"] == "Email, password and name are required fields"

    @allure.title("Тестируем, что создание пользователя с пустым полем password возвращает ошибку")
    def test_user_creation_without_password_return_error(self, user_creation):
        credentials = user_creation
        credentials["password"] = ""
        response = UserMethods.user_creation(credentials)
        assert response.status_code == 403
        assert response.json()["success"] == False
        assert response.json()["message"] == "Email, password and name are required fields"

    @allure.title("Тестируем, что создание пользователя с пустым полем name возвращает ошибку")
    def test_user_creation_without_name_return_error(self, user_creation):
        credentials = user_creation
        credentials["name"] = ""
        response = UserMethods.user_creation(credentials)
        assert response.status_code == 403
        assert response.json()["success"] == False
        assert response.json()["message"] == "Email, password and name are required fields"
