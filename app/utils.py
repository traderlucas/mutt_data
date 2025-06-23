from datetime import datetime

crypto_lista = [ "bitcoin", "ethereum", "tether", "xrp", "bnb", "solana", "usd coin", "tron", "dogecoin", "lido staked ether", "cardano", "wrapped bitcoin", "hyperliquid", "wrapped steth", "bitcoin cash", "sui", "leo token", "chainlink", "stellar", "avalanche", "toncoin", "polkadot", "near protocol", "uniswap", "dai", "litecoin", "kaspa", "ethereum classic", "internet computer", "pepe", "fetch.ai", "render", "shiba inu", "immutable", "stacks", "optimism", "cronos", "aptos", "vechain", "arbitrum", "maker", "hedera", "the graph", "first digital usd", "quant", "mantle", "okb", "algorand", "celestia", "sei", "fantom", "synthetix", "rocket pool eth", "ecash", "chiliz", "thorchain", "ordi", "monero", "beam", "jasmycoin", "flare", "bitget token", "aave", "multiversx", "ondo", "singularitynet", "gnosis", "conflux", "usdd", "worldcoin", "helium", "curve dao token", "axie infinity", "kucoin token", "frax", "zcash", "tezos", "tokenfi", "oasis network", "iota", "enjin coin", "dydx", "tether gold", "nervos network", "decentraland", "stargate finance", "woo network", "eos", "kava", "gmx", "galxe", "lido dao", "ankr", "reserve rights", "balancer", "blur", "ocean protocol", "gala", "band protocol", "alchemy pay"]

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d-%m-%Y')
        return True
    except ValueError:
        return False
    
def is_valid_end_date(date_string, start_date):
    try:
        end_date = datetime.strptime(date_string, '%d-%m-%Y')
        start_date = datetime.strptime(date_string, '%d-%m-%Y')

        return end_date >= start_date
    except ValueError:
        return False

def is_valid_crypto(crypto):
    return crypto in crypto_lista