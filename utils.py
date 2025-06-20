import requests
from abc import ABC, abstractmethod
import logging
import json
from datetime import timedelta

logger = logging.getLogger(__name__)

class DoRequest(ABC):
    @abstractmethod
    def do_request(self, url, params, token):
        return NotImplementedError("Subclasses must implement this method")


class GetCoinData(DoRequest):
    def __init__(self, coin, date):
        self.coin = coin
        self.date = date
        self.url = f"https://api.coingecko.com/api/v3/coins/{coin}/history?date={date}"
        self.headers = {
            "accept": "application/json",
            "x-cg-pro-api-key": "CG-Lq198PbvigmEDfWB6C5sYUV5"
        }

    def do_request(self):
        logging.info("Getting the data")
        try:
            response = requests.get(url=self.url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except Exception as e:
            print(f"Other Error: {e}")


    def get_data(self):
        return self.do_request()


    def save_data_locally(self):
        data = self.get_data()
        with open(f"temp_data_{self.coin}_{self.date}.json", "w", encoding="utf-8") as temp:
            json.dump(data, temp, ensure_ascii=False, indent=2)


class GetBulkCoinData:
    def __init__(self, coin, start_date, end_date, concurrency=5):
        self.coin = coin
        self.start_date = start_date
        self.end_date = end_date
        self.concurrency = concurrency


    def date_range(self):
        lista = []
        current = self.start_date
        
        while current <= self.end_date:
            lista.append(current)
            current += timedelta(days=1)

        logging.info(f"Total days {len(lista)}")
        return lista
        

    def get_data(self, date):
        downloader = GetCoinData(self.coin, date)
        data = downloader.get_data()


get_data = GetCoinData("bitcoin", "30-12-2024")
result = get_data.save_data_locally()