import requests
from abc import ABC, abstractmethod
import logging
import json
from datetime import timedelta, datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import  sleep

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
            "x-cg-pro-api-key": "CG-hAq6khi4Cc1nhPCNzJroKNEU"
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
    def __init__(self, coin, start_date, end_date, max_workers=5):
        self.coin = coin
        self.start_date = start_date
        self.end_date = end_date
        self.max_workers = max_workers
        self.file_name = f"{self.coin}_data_for_dates_{self.start_date}_to_{self.end_date}.jsonl"
        self.dates_list = self.date_range()
        self.url = f"https://api.coingecko.com/api/v3/coins/{coin}/history"
        self.headers = {
            "accept": "application/json",
            "x-cg-demo-api-key": "CG-Lq198PbvigmEDfWB6C5sYUV5"
        }

    
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
        sleep(5)

        if data:
            data = { "date":date, "data":data}
            with open(self.file_name, "a", encoding="utf-8") as output:
                output.write(json.dumps(data) + "\n")
                logging.info(f"data_for_{date}_saved")
    

    def getting_and_saving_data(self):

        for date in self.dates_list:
            self.process_data(date)

class GetBulkCoinDataInParallel(GetBulkCoinData):
    def __init__(self, coin, start_date, end_date, max_workers=10):
        super().__init__(coin, start_date, end_date, max_workers)

    def getting_and_saving_data(self):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            executor.map(self.process_data, self.dates_list)


# get_data = GetCoinData("bitcoin", "03-01-2025")
# result = get_data.save_data_locally()

# get_data = GetBulkCoinData("bitcoin", "01-01-2025", "30-01-2025")
# get_data.getting_and_saving_data()

get_data = GetBulkCoinDataInParallel("bitcoin", "01-01-2025", "30-01-2025")
get_data.getting_and_saving_data()