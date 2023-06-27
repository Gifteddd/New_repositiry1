import requests


class APIException(Exception):#класс исключения,который поможет нам для обработки ошибок
    pass                      #возникшие при работе с API


class CurrencyConverter:#класс для получения курса валют
    @staticmethod
    def get_price(base: str, quote: str, amount: float) -> float:
        url = f"https://api.exchangerate-api.com/v4/latest/{base}"
        response = requests.get(url)
    # base - валюта, цену которой мы хотим узнать, quote - валюта,
    # в которой мы хотим узнать цену первой валюты, amount - количество первой валюты.    
    #Метод использует API для получения курса валют и возвращает цену во второй валюте.
        if response.status_code != 200:
            raise APIException(f"Не удалось получить курс {base}")

        data = response.json()

        if quote not in data["rates"]:
            raise APIException(f"Не удалось получить курс {quote}")

        rate = data["rates"][quote]
        return rate * amount
