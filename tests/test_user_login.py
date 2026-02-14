import allure
from generators import *
from methods.user_methods import UserMethods


class TestUserLogin:

    @allure.title("Тестируем, что пользователь успешно логинится")
    def test_user_login_success(self, user_login):
        credentials = user_login
        response = UserMethods.user_login(credentials)
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "refreshToken" in response.json()

    @allure.title("Тестируем, что пользователь не может залогиниться, если передать неправильный email")
    def test_user_login_with_wrong_email_return_error(self, user_login):
        credentials = user_login
        credentials["email"] = "abcdfdgdgdfbfb@yyyy.tt"
        response = UserMethods.user_login(credentials)
        assert response.status_code == 401
        assert response.json()["success"] == False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Тестируем, что пользователь не может залогиниться, если передать неправильный password")
    def test_user_login_with_wrong_password_return_error(self, user_login):
        credentials = user_login
        credentials["password"] = "abcdfdgdgdfbfb576557575fhgcfg"
        response = UserMethods.user_login(credentials)
        assert response.status_code == 401
        assert response.json()["success"] == False
        assert response.json()["message"] == "email or password are incorrect"
    