import pytest
import allure

from methods.courier_methods import CourierMethods
from data import Data

class TestCourier:

    @allure.title('Cоздание курьера')
    def test_create_courier(self):
        response = CourierMethods().create_new_courier()
        assert response == (201, '{"ok":true}')

    @allure.title('Создание курьера с обязательными полями')
    def test_create_courie_with_required_fields(self):
        response = CourierMethods().request_to_create_courier(Data.payload_3)
        assert response == (201, '{"ok":true}')

    @allure.title('Запрос на создние курьера с пустыми полями')
    @pytest.mark.parametrize('payload', [Data.payload_1, Data.payload_2])
    def test_incorrect_data_for_create_courier(self, payload):
        response = CourierMethods().request_to_create_courier(payload)
        assert response == (400, '{"code":400,"message":"Недостаточно данных для создания учетной записи"}')

    @allure.title('Cоздание пользователя с существующим логином')
    def test_create_existing_courier(self):
        response = CourierMethods().create_existing_courier()
        assert response == (409, '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}')
