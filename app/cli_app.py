import logging
from utils import *

logger = logging.getLogger(__name__)

def get_crypto():
    while True:
        coin_input = input("Please enter a crypto currency: ").lower()
        if is_valid_crypto(coin_input):
            logger.info(f"You entered a valid coin: {coin_input}")
            return coin_input
        else:
            logger.warning("Invalid coin entered.")
            logger.info("Valid coins are bitcoin, ethereum, tether, solana, cardano")

def get_start_date():
    while True:
        date_input = input("Please enter a start date (yyyy-mm-dd): ")
        if is_valid_date(date_input):
            logger.info(f"You entered a valid date: {date_input}")
            return date_input
        else:
            logger.warning("Invalid start date format or date.")
            logger.info("Remember the format is yyyy-mm-dd.")

def get_end_date(start_date):
    while True:
        date_input = input("Please enter an end date (optional), blank for the same as start_date: ") or start_date
        if is_valid_date(date_input):
            logger.info(f"End date equals: {date_input}")
            return date_input
        else:
            logger.warning("Invalid end date format or date.")
            logger.info("Remember the format is yyyy-mm-dd.")

def persist_data():
    while True:
        persist = input("Would you like to persist the data in a database (y/n): ").lower()
        if persist == "y":
            logger.info("Persisting data in Postgres Database")
            return True
        else:
            logger.info("Exiting app, data not saved in Database")
            return False
