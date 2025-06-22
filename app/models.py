from sqlalchemy import Column, Integer, String, Date, Numeric, JSON, UniqueConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CoinHistory(Base):
    __tablename__ = 'coin_history'
    coin_id = Column(String, primary_key=True, nullable=False)
    date = Column(Date, primary_key=True, nullable=False)
    price_usd = Column(Numeric)
    raw_json = Column(JSON)
    __table_args__ = (UniqueConstraint("coin_id", "date"),)

class CoinAggregate(Base):
    __tablename__ = 'coin_aggregates'
    coin_id = Column(String, primary_key=True, nullable=False)
    year = Column(Integer, primary_key=True, nullable=False)
    month = Column(Integer, primary_key=True, nullable=False)
    max_price = Column(Numeric)
    min_price = Column(Numeric)
    __table_args__ = (UniqueConstraint("coin_id", "year", "month"),)
