import requests
from url import URL
import allure

class UserMethods:

    @staticmethod
    def user_creation(credentials):
        return requests.post(URL.USER_CREATION_URL, json = credentials)
        
    @staticmethod
    def user_login(credentials):
        return requests.post(URL.USER_LOGIN_URL, json = credentials)
      