import requests
import allure

from config import BASE_URL, COURIERS_URL
from helpers import Helpers

class CourierMethods:

    @allure.step('Запрос на создание курьера')
    def request_to_create_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return response.status_code, response.text

    @allure.step('Cоздание нового курьера')
    def create_new_courier(self):
        payload = Helpers().register_new_courier()
        response = self.request_to_create_courier(payload)
        return response

    @allure.step('Создание курьера с существующим логином')
    def create_existing_courier(self):
        payload = Helpers().register_new_courier()
        self.request_to_create_courier(payload)
        response = self.request_to_create_courier(payload)
        return response

    @allure.step('Запрос на авторизацию курьера')
    def request_to_autorization_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', data=payload)
        return response.text

    @allure.step('Авторизация курьера c передачей обязательных полей')
    def authorization_courier(self):
        payload = Helpers().register_new_courier()
        requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        payload_1 = {
            "login": payload['login'],
            "password": payload['password']
        }
        return payload_1

    @allure.step('Авторизация несуществующего курьера')
    def authorization_non_existent_courier(self):
        payload = Helpers().register_new_courier()
        response = self.request_to_autorization_courier(payload)
        return response


