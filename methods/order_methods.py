import requests
import allure

from config import BASE_URL, COURIERS_URL, ORDER_URL
from methods.courier_methods import CourierMethods

class OrderMethods:

    @allure.step('Создание заказа')
    def place_order(self, payload):
        response = requests.post(f'{BASE_URL}{ORDER_URL}', data=payload)
        return response.text

    @allure.step('Получение списка заказов')
    def get_list_orders(self, id):
        response = requests.get(f'{BASE_URL}{ORDER_URL}?courierId={id}')
        return response.text

    @allure.step('Получение id курьера')
    def create_couriers_order(self):
        payload = CourierMethods().authorization_courier()
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', data=payload)
        return response.json()["id"]
