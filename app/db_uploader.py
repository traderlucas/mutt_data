import json
from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base, CoinHistory
import logging

logger = logging.getLogger(__name__)

class DBUploader:
    def __init__(self, db_url="postgresql://postgres:postgres@localhost:5432/crypto"):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def init_db(self):
        Base.metadata.create_all(self.engine)

    def insert_coin_history(self, coin_id, date, price, raw_json):
        record = CoinHistory(
            coin_id=coin_id,
            date=date,
            price_usd=price,
            raw_json=raw_json
        )
        self.session.merge(record)

    def process_file(self, file_path):
        logger.info(f"Inserting {file_path} data into Database")
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                record = json.loads(line)
                date_str = record["date"]
                raw_data = record["data"]
                coin_id = raw_data.get("id", {})
                price = raw_data.get("market_data", {}).get("current_price", {}).get("usd")
                date = datetime.strptime(date_str, "%d-%m-%Y").date()
                self.insert_coin_history(coin_id, date, price, raw_data)
        self.session.commit()
        logger.info("Coins successfully inserted in the Database")

    def run_aggregation_sql(self, sql_path="app/sql/update_aggregates.sql"):
        with self.engine.begin() as conn:
            with open(sql_path) as f:
                sql = f.read()
                conn.execute(text(sql))


    def close(self):
        self.session.close()
