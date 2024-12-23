import allure

from methods.courier_methods import CourierMethods
from data import Response
from helpers import Helpers

class TestAuthorization:

    @allure.title('Авторизация курьера')
    def test_authorization_courier(self):
        data_payload = Helpers().register_new_courier()
        payload = CourierMethods().authorization_courier_data(data_payload)
        response = CourierMethods().request_to_authorization_courier(payload)
        assert "id" in response.text and response.status_code == 200

    @allure.title('Авторизация несуществующего курьера')
    def test_authorization_non_existent_courier(self):
        response = CourierMethods().authorization_non_existent_courier()
        assert response.text == Response.massage_non_existent_courier and response.status_code == 404

    @allure.title('Запрос на авторизацию курьера с неуказанным логином')
    def test_empty_login_for_create_courier(self):
        data_payload = Helpers().register_new_courier()
        payload = CourierMethods().authorization_courier_data(data_payload)
        payload_1 = {
            "login": '',
            "password": payload['password']
        }
        response = CourierMethods().request_to_authorization_courier(payload_1)
        assert response.text == Response.error_empty_field and response.status_code == 400

    @allure.title('Запрос на авторизацию курьера с неуказанным паролем')
    def test_empty_password_for_create_courier(self):
        data_payload = Helpers().register_new_courier()
        payload = CourierMethods().authorization_courier_data(data_payload)
        payload_1 = {
            "login": payload['login'],
            "password": ''
        }
        response = CourierMethods().request_to_authorization_courier(payload_1)
        assert response.text == Response.error_empty_field and response.status_code == 400

    @allure.title('Запрос на авторизацию курьера с ошибочным логином')
    def test_incorrect_login_for_create_courier(self):
        data_payload = Helpers().register_new_courier()
        payload = CourierMethods().authorization_courier_data(data_payload)
        payload_1 = {
            "login": 'klava',
            "password": payload['password']
            }
        response = CourierMethods().request_to_authorization_courier(payload_1)
        assert response.text == Response.error_incorrect_login and response.status_code == 404

    @allure.title('Запрос на авторизацию курьера с ошибочным логином')
    def test_incorrect_password_for_create_courier(self):
        data_payload = Helpers().register_new_courier()
        payload = CourierMethods().authorization_courier_data(data_payload)
        payload_1 = {
            "login": payload['login'],
            "password": '258963'
        }
        response = CourierMethods().request_to_authorization_courier(payload_1)
        assert response.text == Response.error_incorrect_login and response.status_code == 404