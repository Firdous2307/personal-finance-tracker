import json

def save_currency_symbol(symbol):
    config = {
        'DB_FILE': 'finance_tracker.db',
        'DATE_FORMAT': '%Y-%m-%d %H:%M:%S',
        'CURRENCY_SYMBOL': symbol
    }
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file)

def load_currency_symbol():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            return config.get('CURRENCY_SYMBOL', '$')
    except FileNotFoundError:
        return '$'
