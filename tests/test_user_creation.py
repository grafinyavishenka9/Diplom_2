import allure
from generators import *
from methods.user_methods import UserMethods
from data import DataForResponseMessages

class TestUserCreation:

    @allure.title("Тестируем, что пользователь успешно создаётся")
    @allure.description('Успешная регистрация нового пользователя при заполнении обязательных полей')
    @allure.step("Тестируем, что пользователь успешно создаётся")
    def test_user_creation_success(self, user_creation):
        credentials = user_creation
        response = UserMethods.user_creation(credentials)
        assert response.status_code == 200
        assert response.json()["success"] == DataForResponseMessages.SUCCESS
            
    @allure.title("Тестируем, что нельзя создать двух одинаковых пользователей")
    @allure.description('Неуспешная регистрация при использовании данных уже зарегистрированного пользователя')
    @allure.step("Тестируем, что нельзя создать двух одинаковых пользователей")
    def test_user_creation_with_same_credentials_not_possible(self, user_creation):
        credentials = user_creation
        response = UserMethods.user_creation(credentials)
        response = UserMethods.user_creation(credentials)
        assert response.status_code == 403
        assert response.json()["message"] == DataForResponseMessages.USER_EXIST

    @allure.title("Тестируем, что создание пользователя с пустым полем email возвращает ошибку")
    @allure.description('Неуспешная регистрация при пустом поле email')
    @allure.step("Тестируем, что создание пользователя с пустым полем email возвращает ошибку")
    def test_user_creation_without_email_return_error(self, user_creation):
        credentials = user_creation
        credentials["email"] = ""
        response = UserMethods.user_creation(credentials)
        assert response.status_code == 403
        assert response.json()["message"] == DataForResponseMessages.EMPTY_FIELD

    @allure.title("Тестируем, что создание пользователя с пустым полем password возвращает ошибку")
    @allure.description('Неуспешная регистрация при пустом поле password')
    @allure.step("Тестируем, что создание пользователя с пустым полем password возвращает ошибку")
    def test_user_creation_without_password_return_error(self, user_creation):
        credentials = user_creation
        credentials["password"] = ""
        response = UserMethods.user_creation(credentials)
        assert response.status_code == 403
        assert response.json()["message"] == DataForResponseMessages.EMPTY_FIELD

    @allure.title("Тестируем, что создание пользователя с пустым полем name возвращает ошибку")
    @allure.description('Неуспешная регистрация при пустом поле name')
    @allure.step("Тестируем, что создание пользователя с пустым полем name возвращает ошибку")
    def test_user_creation_without_name_return_error(self, user_creation):
        credentials = user_creation
        credentials["name"] = ""
        response = UserMethods.user_creation(credentials)
        assert response.status_code == 403
        assert response.json()["message"] == DataForResponseMessages.EMPTY_FIELD
