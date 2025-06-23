from extractor import *
from cli_app import *
from db_uploader import *
from datetime import datetime
    
def main():
    coin = get_crypto()
    start_date = get_start_date()
    end_date = get_end_date(start_date)
    
    extractor = GetBulkCoinDataInParallel(coin, start_date, end_date)
    extractor.getting_and_saving_data()
    data_path = extractor.get_path()

    # persist = persist_data()

    # if persist:
    #     uploader = DBUploader()
    #     uploader.init_db()
    #     uploader.process_file(data_path)
    #     uploader.run_aggregation_sql()



if __name__ == "__main__":
    main()
