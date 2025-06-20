import requests
from abc import ABC, abstractmethod

class DoRequest(ABC):
    @abstractmethod
    def do_request(self, url, params, token):
        return NotImplementedError("Subclasses must implement this method")


class GetCoinData(DoRequest):
    def __init__(self, coin, date):
        self.url = f"https://api.coingecko.com/api/v3/coins/{coin}/history?date={date}"
        self.headers = {
            "accept": "application/json",
            "x-cg-pro-api-key": "CG-Lq198PbvigmEDfWB6C5sYUV5"
        }

    def do_request(self):
        try:
            response = requests.get(url=self.url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except Exception as e:
            print(f"Other Error: {e}")

get_data = GetCoinData("bitcoin", "30-12-2024")
result = get_data.do_request()