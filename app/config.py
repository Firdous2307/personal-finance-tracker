import json
import os

def save_currency_symbol(symbol):
    config = {
        'DB_FILE': 'finance_tracker.db',
        'DATE_FORMAT': '%Y-%m-%d %H:%M:%S',
        'CURRENCY_SYMBOL': symbol,
        'AWS_SNS_TOPIC_ARN': os.getenv('AWS_SNS_TOPIC_ARN', '')
    }
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file)

def load_config():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        return {'CURRENCY_SYMBOL': '$', 'AWS_SNS_TOPIC_ARN': ''}


config = load_config()

CURRENCY_SYMBOL = config.get('CURRENCY_SYMBOL', '$')
AWS_SNS_TOPIC_ARN = config.get('AWS_SNS_TOPIC_ARN', '')
