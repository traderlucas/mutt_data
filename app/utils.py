from datetime import datetime

crypto_lista = ["bitcoin", "ethereum", "cardano", "solana"]

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d-%m-%Y')
        return True
    except ValueError:
        return False
    
def is_valid_crypto(crypto):
    return crypto in crypto_lista