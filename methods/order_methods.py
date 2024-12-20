import requests
import allure

from config import BASE_URL, COURIER_LOGIN, ORDER_URL, COURIER_ID, CANCEL_ORDER
from methods.courier_methods import CourierMethods
from data import Data

class OrderMethods:

    @allure.step('Создание заказа')
    def place_order(self, payload):
        response = requests.post(f'{BASE_URL}{ORDER_URL}', data=payload)
        return response

    @allure.step('Отмена заказа')
    def cancel_order(self, track):
        payload = {"track": track}
        response = requests.put(f'{BASE_URL}{CANCEL_ORDER}', data=payload)
        return response

    @allure.step('Получение списка заказов')
    def get_list_orders(self, courier_id):
        response = requests.get(f'{BASE_URL}{COURIER_ID}{courier_id}')
        return response

    @allure.step('Получение id курьера')
    def create_couriers_order(self):
        payload = CourierMethods().authorization_courier_data(Data.authorization)
        response = requests.post(f'{BASE_URL}{COURIER_LOGIN}', data=payload)
        return response.json()["id"]
