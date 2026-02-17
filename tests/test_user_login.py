import allure
from generators import *
from methods.user_methods import UserMethods
from data import DataForResponseMessages

class TestUserLogin:

    @allure.title("Тестируем, что пользователь успешно логинится")
    @allure.description('Успешный вход в аккаунт зарегистрированного пользователя')
    @allure.step("Тестируем, что пользователь успешно логинится")
    def test_user_login_success(self, user_login):
        credentials = user_login
        response = UserMethods.user_login(credentials)
        assert response.status_code == 200
        assert response.json()["success"] == DataForResponseMessages.SUCCESS
        

    @allure.title("Тестируем, что пользователь не может залогиниться, если передать неправильный email")
    @allure.description('Неуспешный вход в аккаунт зарегистрированного пользователя с неправильно указанным email')
    @allure.step("Тестируем, что пользователь не может залогиниться, если передать неправильный email")
    def test_user_login_with_wrong_email_return_error(self, user_login):
        credentials = user_login
        credentials["email"] = "abcdfdgdgdfbfb@yyyy.tt"
        response = UserMethods.user_login(credentials)
        assert response.status_code == 401
        assert response.json()["message"] == DataForResponseMessages.WRONG_FIELD

    @allure.title("Тестируем, что пользователь не может залогиниться, если передать неправильный password")
    @allure.description('Неуспешный вход в аккаунт зарегистрированного пользователя с неправильно указанным password')
    @allure.step("Тестируем, что пользователь не может залогиниться, если передать неправильный password")
    def test_user_login_with_wrong_password_return_error(self, user_login):
        credentials = user_login
        credentials["password"] = "abcdfdgdgdfbfb576557575fhgcfg"
        response = UserMethods.user_login(credentials)
        assert response.status_code == 401
        assert response.json()["message"] == DataForResponseMessages.WRONG_FIELD
    