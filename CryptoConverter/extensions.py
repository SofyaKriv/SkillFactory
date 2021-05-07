
import requests
import json
from config import keys


class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        # r = requests.get(f'https://api.exchangeratesapi.io/v1/convert?access_key=2cd3ba9b6c10ca874c1fbad89b17f672&from={quote_ticker}&to={base_ticker}&amount={amount}')
        # r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        r = requests.get(f'https://currate.ru/api/?get=rates&pairs={quote_ticker}{base_ticker}&key=71b25bae98527bd30499c7355d15497f')
        str1 = quote_ticker + base_ticker
        total_base = float(json.loads(r.content)['data'][str1]) * float(amount)
        return total_base

