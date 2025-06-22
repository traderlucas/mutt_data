from extractor import *
from cli_app import *
from db_uploader import *
from datetime import datetime
    
def main():
    coin = get_crypto()
    # start_date = get_start_date()
    # end_date = get_end_date(start_date)

    # coin = "solana"
    start_date = "01-01-2025"
    end_date = "30-01-2025"
    
    if start_date == end_date:
        extractor = GetCoinData(coin, start_date)
        extractor.save_data_locally()
        data_path = extractor.get_path()
    else: #limited by the API 30 requests
        extractor = GetBulkCoinDataInParallel(coin, start_date, end_date)
        #extractor = GetBulkCoinData(coin, start_date, end_date) 
        extractor.getting_and_saving_data()
        data_path = extractor.get_path()

    uploader = DBUploader()
    uploader.init_db()
    uploader.process_file(data_path)
    uploader.run_aggregation_sql()



if __name__ == "__main__":
    main()


# def process_file(file_path):
#     with open(file_path, "r", encoding="utf-8") as f:
#         for line in f:
#             record = json.loads(line)
#             date_str = record["date"]
#             raw_data = record["data"]
#             coin_id = raw_data.get("id", {})
#             price = raw_data.get("market_data", {}).get("current_price", {}).get("usd")
#             if not price:
#                 continue
#             date = datetime.strptime(date_str, "%d-%m-%Y").date()
#             print(coin_id, date, price, raw_data)

# if __name__ == "__main__":
#     process_file("app/data/bitcoin_data_for_dates_01-01-2025_to_30-01-2025.jsonl")
