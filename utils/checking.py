"""Методы для проверки ответов наших запросов"""
import json

from requests import Response


class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code  #Слева ожидаем, справа то что получаем
        if response.status_code == status_code:
            print("Успешно!!! Статус код = " + str(response.status_code))
        else:
            print("Провал!!! Статус код = " + str(response.status_code))



    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)   #функция loads модуля json преобразует строку в формат json.
        assert list(token) == expected_value
        print("Все поля присутствуют!!!")
