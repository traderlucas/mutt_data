import json
from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base, CoinHistory

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/crypto"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def insert_coin_history(session, coin_id, date, price, raw_json):
    record = CoinHistory(
        coin_id=coin_id,
        date=date,
        price_usd=price,
        raw_json=raw_json
    )
    session.merge(record)

def process_file(file_path, coin_id):
    session = Session()
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            record = json.loads(line)
            date_str = record["date"]
            raw_data = record["data"]
            price = raw_data.get("market_data", {}).get("current_price", {}).get("usd")
            if not price:
                continue
            date = datetime.strptime(date_str, "%d-%m-%Y").date()
            insert_coin_history(session, coin_id, date, price, raw_data)
    session.commit()
    session.close()

def run_sql_aggregate(sql_path="sql/update_aggregates.sql"):
    with engine.connect() as conn:
        with open(sql_path) as f:
            conn.execute(text(f.read()))
