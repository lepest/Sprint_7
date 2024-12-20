import requests
import allure
import json

from config import BASE_URL, COURIERS_URL, COURIER_LOGIN, DELETE_COURIER
from helpers import Helpers

class CourierMethods:

    @allure.step('Запрос на создание курьера')
    def request_to_create_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return response

    @allure.step('Cоздание нового курьера')
    def create_new_courier(self):
        payload = Helpers().register_new_courier()
        response = self.request_to_create_courier(payload)
        return response

    @allure.step('Получение данных для авторизация курьера')
    def authorization_courier_data(self, payload):
        requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        login = payload["login"]
        password = payload["password"]
        payload_1 = {
            "login": login,
            "password": password
        }
        return payload_1

    @allure.step('Авторизация курьера c передачей обязательных полей')
    def authorization_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIER_LOGIN}', data=payload)
        return response.json()["id"]

    @allure.step('Удаление курьера')
    def delete_courier(self, payload):
        authorization_payload = self.authorization_courier_data(payload)
        courier_id = self.authorization_courier(authorization_payload)
        response = requests.delete(f'{BASE_URL}{DELETE_COURIER}{courier_id}', data=payload)
        return response

    @allure.step('Создание курьера с существующим логином')
    def create_existing_courier(self):
        payload = Helpers().register_new_courier()
        self.request_to_create_courier(payload)
        response = self.request_to_create_courier(payload)
        return response

    @allure.step('Запрос на авторизацию курьера')
    def request_to_authorization_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIER_LOGIN}', data=payload)
        return response

    @allure.step('Авторизация несуществующего курьера')
    def authorization_non_existent_courier(self):
        payload = Helpers().register_new_courier()
        response = self.request_to_authorization_courier(payload)
        return response





