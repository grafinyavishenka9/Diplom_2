import allure
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods
from data import DataForResponseMessages, DataForOrderCreation

class TestOrderCreation:

    @allure.title("Тестируем создание заказа без авторизации")
    @allure.description('Создание заказа')
    @allure.step("Тестируем создание заказа без авторизации")
    def test_order_creation_without_authentication(self, order_creation):
        response = OrderMethods.order_creation(order_creation)
        assert response.status_code == 200
        assert response.json()["success"] == DataForResponseMessages.SUCCESS

    @allure.title("Тестируем создание заказа с авторизацией")
    @allure.description('Успешное создание заказа с авторизацией')
    @allure.step("Тестируем создание заказа с авторизацией")
    def test_order_creation_with_authentication(self, user_login, order_creation):
        credentials = user_login
        response_login = UserMethods.user_login(credentials)
        response = OrderMethods.order_creation(order_creation)
        assert response_login.status_code == 200
        assert response_login.json()["success"] == True
        assert "refreshToken" in response_login.json()
        assert response.status_code == 200
        assert response.json()["success"] == DataForResponseMessages.SUCCESS

    @allure.title("Тестируем создание заказа c ингредиентами")
    @allure.description('Успешное создание заказа с ингридиентами')
    @allure.step("Тестируем создание заказа c ингредиентами")
    def test_order_creation_with_ingredients(self, order_creation):
        response = OrderMethods.order_creation(order_creation)
        assert response.status_code == 200
        assert response.json()["success"] == DataForResponseMessages.SUCCESS

    @allure.title("Тестируем создание заказа без ингредиентов")
    @allure.description('Неуспешное создание заказа без ингридиентов')
    @allure.step("Тестируем создание заказа без ингредиентов")
    def test_order_creation_without_ingredients(self):
        credentials = {}
        response = OrderMethods.order_creation(credentials)
        assert response.status_code == 400
        assert response.json()["message"] == DataForResponseMessages.ORDER_WITHOUT_INGREDIENTS

    @allure.title("Тестируем создание заказа с неверным хэшем ингридиентов")
    @allure.description('Неуспешное создание заказа с неверным хешем ингридиентов')
    @allure.step("Тестируем создание заказа с неверным хэшем ингридиентов")
    def test_order_creation_with_wrong_ingredients_hash(self):
        credentials = DataForOrderCreation.CREATE_ORDER_WRONG_DATA
        response = OrderMethods.order_creation(credentials)
        assert response.status_code == 500
           