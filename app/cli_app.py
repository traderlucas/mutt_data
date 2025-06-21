from utils import *


def get_crypto():
    "valid_crypto https://www.coingecko.com/en/all-cryptocurrencies"

    while True:
        date_input = input("Please enter a date (dd-mm-yyyy): ")
        if is_valid_crypto(date_input):
            print(f"You entered a valid date: {date_input}")
            return(date_input)
        else:
            print("Invalid date format or date. Please try again.")
            print("Remember the format is dd-mm-yyyy (e.g., 25-12-2024).")
    

def get_start_date():
    while True:
        date_input = input("Please enter a start date (dd-mm-yyyy): ")
        if is_valid_date(date_input):
            print(f"You entered a valid date: {date_input}")
            return(date_input)
        else:
            print("Invalid date format or date. Please try again.")
            print("Remember the format is dd-mm-yyyy (e.g., 25-12-2024).")
    
def get_end_date():
    while True:
        date_input = input("Please enter a end date (dd-mm-yyyy): ")
        if is_valid_date(date_input):
            print(f"You entered a valid date: {date_input}")
            return(date_input)
        else:
            print("Invalid date format or date. Please try again.")
            print("Remember the format is dd-mm-yyyy (e.g., 25-12-2024)")

def persist_data():
    pass