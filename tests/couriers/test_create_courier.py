import pytest
import allure

from methods.courier_methods import CourierMethods
from data import Data
from data import Response
from helpers import Helpers

class TestCourier:

    @allure.title('Cоздание курьера')
    def test_create_courier(self):
        payload = Data.payload_3
        response = CourierMethods().request_to_create_courier(payload)
        assert response.text == Response.success_massage and response.status_code == 201
        CourierMethods().delete_courier(payload)

    @allure.title('Создание курьера с обязательными полями')
    def test_create_courie_with_required_fields(self):
        payload = Helpers().register_new_courier()
        response = CourierMethods().request_to_create_courier(payload)
        assert response.text == Response.success_massage and response.status_code == 201
        CourierMethods().delete_courier(payload)

    @allure.title('Запрос на создние курьера с пустыми полями')
    @pytest.mark.parametrize('payload', [Data.payload_1, Data.payload_2])
    def test_incorrect_data_for_create_courier(self, payload):
        response = CourierMethods().request_to_create_courier(payload)
        assert response.text == Response.massage_empty_fields and response.status_code == 400

    @allure.title('Cоздание пользователя с существующим логином')
    def test_create_existing_courier(self):
        response = CourierMethods().create_existing_courier()
        assert response.status_code == 409 and response.text == Response.massage_existing_courier
