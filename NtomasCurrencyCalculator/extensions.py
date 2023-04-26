import requests
import json
from config import currency_dict


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = currency_dict[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = currency_dict[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException('Неправильно введено число')
        r = requests.get(
            'https://min-api.cryptocompare.com/data/price?fsym=' +
            f'{quote_ticker}&tsyms={base_ticker}'
        )
        total_base = json.loads(r.content)[currency_dict[base]]
        return total_base * amount
