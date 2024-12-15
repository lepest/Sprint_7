import allure

from methods.courier_methods import CourierMethods

class TestAuthorization:

    @allure.title('Авторизация курьера')
    def test_authorization_courier(self):
        payload = CourierMethods().authorization_courier()
        response = CourierMethods().request_to_autorization_courier(payload)
        assert "id" in response

    @allure.title('Авторизация несуществующего курьера')
    def test_authorization_non_existent_courier(self):
        response = CourierMethods().authorization_non_existent_courier()
        assert response == '{"code":404,"message":"Учетная запись не найдена"}'

    @allure.title('Запрос на авторизацию курьера с неуказанным логином')
    def test_empty_login_for_create_courier(self):
        payload = CourierMethods().authorization_courier()
        payload_1 = {
            "login": '',
            "password": payload['password']
        }
        response = CourierMethods().request_to_autorization_courier(payload_1)
        assert response == '{"code":400,"message":"Недостаточно данных для входа"}'

    @allure.title('Запрос на авторизацию курьера с неуказанным паролем')
    def test_empty_password_for_create_courier(self):
        payload = CourierMethods().authorization_courier()
        payload_1 = {
            "login": payload['login'],
            "password": ''
        }
        response = CourierMethods().request_to_autorization_courier(payload_1)
        assert response == '{"code":400,"message":"Недостаточно данных для входа"}'

    @allure.title('Запрос на авторизацию курьера с ошибочным логином')
    def test_incorrect_login_for_create_courier(self):
        payload = CourierMethods().authorization_courier()
        payload_1 = {
            "login": 'klava',
            "password": payload['password']
            }
        response = CourierMethods().request_to_autorization_courier(payload_1)
        assert response == '{"code":404,"message":"Учетная запись не найдена"}'

    @allure.title('Запрос на авторизацию курьера с ошибочным логином')
    def test_incorrect_password_for_create_courier(self):
        payload = CourierMethods().authorization_courier()
        payload_1 = {
            "login": payload['login'],
            "password": '258963'
        }
        response = CourierMethods().request_to_autorization_courier(payload_1)
        assert response == '{"code":404,"message":"Учетная запись не найдена"}'