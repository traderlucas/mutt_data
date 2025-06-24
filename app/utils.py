from datetime import datetime

crypto_lista = [ "bitcoin", "ethereum", "tether", "bnb", "solana", "cardano"]

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def is_valid_end_date(date_string, start_date):
    try:
        end_date = datetime.strptime(date_string, '%Y-%m-%d')
        start_date = datetime.strptime(date_string, '%Y-%m-%d')
        return end_date >= start_date
    except ValueError:
        return False

def is_valid_crypto(crypto):
    return crypto in crypto_lista

def app_art(f):
    def wrapper():
        init_cli_app()
        try:
            f()
        finally:
            finish_cli_app
    return wrapper

def init_cli_app():
    print("""
        
███╗   ███╗██╗   ██╗████████╗████████╗    ██████╗  █████╗ ████████╗ █████╗  
████╗ ████║██║   ██║╚══██╔══╝╚══██╔══╝    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗ 
██╔████╔██║██║   ██║   ██║      ██║       ██║  ██║███████║   ██║   ███████║ 
██║╚██╔╝██║██║   ██║   ██║      ██║       ██║  ██║██╔══██║   ██║   ██╔══██║ 
██║ ╚═╝ ██║╚██████╔╝   ██║      ██║       ██████╔╝██║  ██║   ██║   ██║  ██║ 
╚═╝     ╚═╝ ╚═════╝    ╚═╝      ╚═╝       ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ 

    """)

def finish_cli_app():
    print("""
███████╗██╗███╗   ██╗██╗███████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║████╗  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗
█████╗  ██║██╔██╗ ██║██║███████╗███████║█████╗  ██║  ██║
██╔══╝  ██║██║╚██╗██║██║╚════██║██╔══██║██╔══╝  ██║  ██║
██║     ██║██║ ╚████║██║███████║██║  ██║███████╗██████╔╝
╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ 
                                                        
""")
    