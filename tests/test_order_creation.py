import allure
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


class TestOrderCreation:

    @allure.title("Тестируем создание заказа без авторизации")
    def test_order_creation_without_authentication(self, order_creation):
        response = OrderMethods.order_creation(order_creation)
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "name" in response.json()
        assert "order" in response.json()

    @allure.title("Тестируем создание заказа с авторизацией")
    def test_order_creation_with_authentication(self, user_login, order_creation):
        credentials = user_login
        response_login = UserMethods.user_login(credentials)
        response = OrderMethods.order_creation(order_creation)
        assert response_login.status_code == 200
        assert response_login.json()["success"] == True
        assert "refreshToken" in response_login.json()
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "name" in response.json()
        assert "order" in response.json()

    @allure.title("Тестируем создание заказа c ингредиентами")
    def test_order_creation_with_ingredients(self, order_creation):
        response = OrderMethods.order_creation(order_creation)
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "name" in response.json()
        assert "order" in response.json()

    @allure.title("Тестируем создание заказа без ингредиентов")
    def test_order_creation_without_ingredients(self):
        credentials = {}
        response = OrderMethods.order_creation(credentials)
        assert response.status_code == 400
        assert response.json()["success"] == False
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Тестируем создание заказа с неверным хэшем ингридиентов")
    def test_order_creation_with_wrong_ingredients_hash(self):
        credentials = {
                    "ingredients":["61c0c5a71d1f82001bdaaa6","61c0c5a71d1f82001bdaaa6fa"]
                    }
        response = OrderMethods.order_creation(credentials)
        assert response.status_code == 500
           