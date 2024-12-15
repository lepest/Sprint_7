from helpers import Helpers

class Data:

    payload = Helpers().register_new_courier()

    payload_1 = {
        "login": '',
        "password": payload['password'],
        "firstName": payload['firstName']
    }

    payload_2 = {
        "login": payload['login'],
        "password": '',
        "firstName": payload['firstName']
    }

    payload_3 = {
        "login": payload['login'],
        "password": payload['password'],
        "firstName": ''
    }

    authorization = {
        "login": payload['login'],
        "password": payload['password'],
        "firstName": payload['firstName']
    }

    data_order_1 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK", ""
        ]
    }

    data_order_2 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "GREY", ""
        ]
    }

    data_order_3 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK", "GREY"
        ]
    }

    data_order_4 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "", ""]
    }