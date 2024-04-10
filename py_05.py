# SOLID: D - Dependency inversion # принцип інверсії залежностей. 
# Модулі от других модулів ніколи не повинні залежати напряму
# Модулі не повинні залежати від модулів нижніх рівнів

import requests


class Connection:
    def get_json(self, url):
        raise NotImplementedError
    

class Request(Connection):
    def __init__(self, request: requests) -> None:
        self.request = request

    def get_json(self, url):
        response = self.request.get(url)
        return response.json()
    

class NewRequest(Connection):
    def get_json(self, url):
        ...

# https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11
class ApiClient:
    def __init__(self, fetch: Connection) -> None:
        self.fetch = fetch

    def get_json(self, url):
        return self.fetch.get_json(url)
    

def pretty_view(data: list[dict]):
    pattern = "|{:^10}|{:^10}|{:^10}|"
    print(pattern.format("currency", "sale", "buy"))
    for el in data:
        currency, *_ = el.keys()
        buy = el.get(currency).get("buy")
        sale = el.get(currency).get("sale")
        print(pattern.format(currency, sale, buy))

def adapter_result_for_pretty_view(data):
    return [{f"{el.get('ccy')}": {"buy": float(el.get('buy')), "sale": float(el.get('sale'))}} for el in data]


if __name__ == "__main__":
    client = ApiClient(Request(requests))
    # client = ApiClient(NewRequest(requests)) новий екземпляр з новою реалізацією передаємо в ApiClient
    data = client.get_json(
        "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )
    pretty_view(adapter_result_for_pretty_view(data))