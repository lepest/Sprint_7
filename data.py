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

    payload_4 = {
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

class Response:

    success_massage = '{"ok":true}'
    massage_empty_fields = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    massage_existing_courier = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    massage_non_existent_courier = '{"code":404,"message":"Учетная запись не найдена"}'
    error_empty_field = '{"code":400,"message":"Недостаточно данных для входа"}'
    error_incorrect_login= '{"code":404,"message":"Учетная запись не найдена"}'

    