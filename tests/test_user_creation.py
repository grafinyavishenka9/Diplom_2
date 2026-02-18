import allure
from generators import *
from methods.user_methods import UserMethods
from data import DataForResponseMessages

class TestUserCreation:

    @allure.title("Тестируем, что пользователь успешно создаётся")
    @allure.description('Успешная регистрация нового пользователя при заполнении обязательных полей')
    def test_user_creation_success(self, user_creation):
        credentials = user_creation
        with allure.step("Создаём пользователя"):
            response = UserMethods.user_creation(credentials)
        assert response.status_code == 200
        assert response.json()["success"] == DataForResponseMessages.SUCCESS
            
    @allure.title("Тестируем, что нельзя создать двух одинаковых пользователей")
    @allure.description('Неуспешная регистрация при использовании данных уже зарегистрированного пользователя')
    def test_user_creation_with_same_credentials_not_possible(self, user_creation):
        credentials = user_creation
        with allure.step("Создаём пользователя"):
            response = UserMethods.user_creation(credentials)
        with allure.step("Создаём пользователя с теми же учётными данными"):
            response = UserMethods.user_creation(credentials)
        assert response.status_code == 403
        assert response.json()["message"] == DataForResponseMessages.USER_EXIST

    @allure.title("Тестируем, что создание пользователя с пустым полем email возвращает ошибку")
    @allure.description('Неуспешная регистрация при пустом поле email')
    def test_user_creation_without_email_return_error(self, user_creation):
        credentials = user_creation
        credentials["email"] = ""
        with allure.step("Создаём пользователя с пустым полем email"):
            response = UserMethods.user_creation(credentials)
        assert response.status_code == 403
        assert response.json()["message"] == DataForResponseMessages.EMPTY_FIELD

    @allure.title("Тестируем, что создание пользователя с пустым полем password возвращает ошибку")
    @allure.description('Неуспешная регистрация при пустом поле password')
    def test_user_creation_without_password_return_error(self, user_creation):
        credentials = user_creation
        credentials["password"] = ""
        with allure.step("Создаём пользователя с пустым полем password"):
            response = UserMethods.user_creation(credentials)
        assert response.status_code == 403
        assert response.json()["message"] == DataForResponseMessages.EMPTY_FIELD

    @allure.title("Тестируем, что создание пользователя с пустым полем name возвращает ошибку")
    @allure.description('Неуспешная регистрация при пустом поле name')
    def test_user_creation_without_name_return_error(self, user_creation):
        credentials = user_creation
        credentials["name"] = ""
        with allure.step("Создаём пользователя с пустым полем name"):
            response = UserMethods.user_creation(credentials)
        assert response.status_code == 403
        assert response.json()["message"] == DataForResponseMessages.EMPTY_FIELD
