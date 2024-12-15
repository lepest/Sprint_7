import pytest
import allure

from methods.order_methods import OrderMethods
from data import Data

class TestOrder:

    @allure.title('Создание заказа')
    @pytest.mark.parametrize('payload', [Data.data_order_1, Data.data_order_2, Data.data_order_3, Data.data_order_4])
    def test_place_order(self, payload):
        response = OrderMethods().place_order(payload)
        assert "track" in response

    @allure.title('Получение списка заказов')
    def test_get_orders_list(self):
        id_courier = OrderMethods().create_couriers_order()
        OrderMethods().place_order(Data.data_order_2)
        response = OrderMethods().get_list_orders(id_courier)
        assert "orders" in response