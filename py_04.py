# SOLID: I - Interface segregation # принцип розділення інтерфейсу
# Сущности не должны зависеть от интерфейсов, которые они не используют

import requests

# https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11
class ApiClient:
    def __init__(self, fetch: requests) -> None:
        self.fetch = fetch

    def get_json(self, url):
        response = self.fetch.get(url)
        return response.json()
    

def pretty_view(data: list[dict]):
    # Було:
    # result = [{f"{el.get('ccy')}": {"buy": float(el.get('buy')), "sale": float(el.get('sale'))}} for el in data]
    # # result это преобразование данных
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
    client = ApiClient(requests)
    data = client.get_json(
        "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )
    pretty_view(adapter_result_for_pretty_view(data))


# "ccy": "EUR",
# "base_ccy": "UAH",
# "buy": "39.08270",
# "sale": "40.65041"

# "ccy": "USD",
# "base_ccy": "UAH",
# "buy": "36.56850",
# "sale": "37.45318"