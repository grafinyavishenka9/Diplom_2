import allure
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods
from data import DataForResponseMessages, DataForOrderCreation

class TestOrderCreation:

    @allure.title("Тестируем создание заказа без авторизации")
    @allure.description('Создание заказа')
    def test_order_creation_without_authentication(self, order_creation):
        with allure.step("Создаём заказ без авторизации"):
            response = OrderMethods.order_creation(order_creation)
        assert response.status_code == 200
        assert response.json()["success"] == DataForResponseMessages.SUCCESS

    @allure.title("Тестируем создание заказа с авторизацией")
    @allure.description('Успешное создание заказа с авторизацией')
    def test_order_creation_with_authentication(self, user_login, order_creation):
        credentials = user_login
        with allure.step("Логинимся пользователем"):
            response_login = UserMethods.user_login(credentials)
        with allure.step("Создаём заказ"):
            response = OrderMethods.order_creation(order_creation)
        assert response.status_code == 200
        assert response.json()["success"] == DataForResponseMessages.SUCCESS

    @allure.title("Тестируем создание заказа c ингредиентами")
    @allure.description('Успешное создание заказа с ингридиентами')
    def test_order_creation_with_ingredients(self, order_creation):
        with allure.step("Создаём заказ с ингредиентами"):
            response = OrderMethods.order_creation(order_creation)
        assert response.status_code == 200
        assert response.json()["success"] == DataForResponseMessages.SUCCESS

    @allure.title("Тестируем создание заказа без ингредиентов")
    @allure.description('Неуспешное создание заказа без ингридиентов')
    def test_order_creation_without_ingredients(self):
        credentials = {}
        with allure.step("Создаём заказ без ингредиентов"):
            response = OrderMethods.order_creation(credentials)
        assert response.status_code == 400
        assert response.json()["message"] == DataForResponseMessages.ORDER_WITHOUT_INGREDIENTS

    @allure.title("Тестируем создание заказа с неверным хэшем ингридиентов")
    @allure.description('Неуспешное создание заказа с неверным хешем ингридиентов')
    def test_order_creation_with_wrong_ingredients_hash(self):
        credentials = DataForOrderCreation.CREATE_ORDER_WRONG_DATA
        with allure.step("Создаём заказ с неверным хешем ингредиентов"):
            response = OrderMethods.order_creation(credentials)
        assert response.status_code == 500
           