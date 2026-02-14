import requests
from url import URL
import allure

class OrderMethods:

    @staticmethod
    def order_creation(credentials):
        with allure.step("Создаём заказ"):
            return requests.post(URL.ORDER_CREATE_URL, json = credentials)
      