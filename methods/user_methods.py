import requests
from url import URL
import allure

class UserMethods:

    @staticmethod
    def user_creation(credentials):
        with allure.step("Создаём пользователя"):
            return requests.post(URL.USER_CREATION_URL, json = credentials)
        
    @staticmethod
    def user_login(credentials):
        with allure.step("Логинимся пользователем"):
            return requests.post(URL.USER_LOGIN_URL, json = credentials)
      