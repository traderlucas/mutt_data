from utils import *


def get_crypto():
    while True:
        coin_input = input("Please enter a crypto currency: ").lower()
        if is_valid_crypto(coin_input):
            print(f"You entered a valid coin: {coin_input}")
            return(coin_input)
        else:
            print("Invalid coin. Please try again.")
            print("link with the valid coins https://www.coingecko.com/en/all-cryptocurrencies")

def get_start_date():
    while True:
        date_input = input("Please enter a start date (dd-mm-yyyy): ")
        if is_valid_date(date_input):
            print(f"You entered a valid date: {date_input}")
            return(date_input)
        else:
            print("Invalid date format or date. Please try again.")
            print("Remember the format is dd-mm-yyyy (e.g., 25-12-2024).")
    
def get_end_date(start_date):
    while True:
        date_input = input("Please enter a end date (optional), blank for the same as start_date: ") or start_date
        if is_valid_date(date_input):
            print(f"End date equals: {date_input}")
            return(date_input)
        else:
            print("Invalid date format or date. Please try again.")
            print("Remember the format is dd-mm-yyyy (e.g., 25-12-2024)")

def persist_data():
    while True:
        persist = input("Would you like to persist the data in a database (y/n): ")
        if persist == "y":
            print("Persisting data in postgres Database")
            return True
        else:
            print("Exiting app, data not saved in Database")
            return False
    