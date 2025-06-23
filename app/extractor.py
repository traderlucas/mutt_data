import requests
from abc import ABC, abstractmethod
import logging
import json
from datetime import timedelta, datetime
from concurrent.futures import ThreadPoolExecutor
import os


API_TOKEN = os.environ["API_TOKEN"]

logger = logging.getLogger(__name__)

class DoRequest(ABC):
    @abstractmethod
    def do_request(self, url, params, token):
        return NotImplementedError("Subclasses must implement this method")

class GetBulkCoinData(DoRequest):
    def __init__(self, coin, start_date, end_date):
        self.coin = coin
        self.start_date = start_date
        self.end_date = end_date
        self.file_name = f"app/data/{self.coin}_{self.start_date}_to_{self.end_date}.jsonl"
        self.dates_list = self.date_range()
        self.url = f"https://api.coingecko.com/api/v3/coins/{coin}/history"
        self.headers = {
            "accept": "application/json",
            "x-cg-demo-api-key": API_TOKEN
        }

    def __str__(self):
        return f"Coin: {self.coin}, start_date: {self.start_date}, end_date: {self.start_date} File: {self.file_name}"
    
    def get_path(self):
        return self.file_name

    def date_range(self):
        lista = []
        current = datetime.strptime(self.start_date, "%d-%m-%Y")

        while current <= datetime.strptime(self.end_date, "%d-%m-%Y"):
            lista.append(current.strftime("%d-%m-%Y"))
            current += timedelta(days=1)

        logging.info(f"Total days {len(lista)}")
        return lista

    def do_request(self, date):
        logging.info("Getting the data")
        params = f"date={date}"
        try:
            response = requests.get(url=self.url, params=params, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        

    def process_data(self, date):
        data = self.do_request(date)
        os.makedirs("app/data", exist_ok=True)

        if data:
            data = { "date":date, "data":data}
            with open(self.file_name, "a", encoding="utf-8") as output:
                output.write(json.dumps(data) + "\n")
                logging.info(f"data_for_{date}_saved")
    

    def getting_and_saving_data(self):
        for date in self.dates_list:
            self.process_data(date)

class GetBulkCoinDataInParallel(GetBulkCoinData):
    def __init__(self, coin, start_date, end_date, max_workers=5):
        super().__init__(coin, start_date, end_date)
        self.max_workers = max_workers

    def getting_and_saving_data(self):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            executor.map(self.process_data, self.dates_list)
