import requests


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: float) -> float:
        url = f"https://api.exchangerate-api.com/v4/latest/{base}"
        response = requests.get(url)

        if response.status_code != 200:
            raise APIException(f"Не удалось получить курс {base}")

        data = response.json()

        if quote not in data["rates"]:
            raise APIException(f"Не удалось получить курс {quote}")

        rate = data["rates"][quote]
        return rate * amount
