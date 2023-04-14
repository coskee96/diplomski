from datetime import datetime, timedelta

CRYPTO_OPTIONS = [
       {'label': 'Bitcoin', 'value': 'bitcoin'},
    {'label': 'Ethereum', 'value': 'ethereum'},
    {'label': 'Ripple (XRP)', 'value': 'xrp'},
    {'label': 'Litecoin', 'value': 'litecoin'},
    {'label': 'Cardano', 'value': 'cardano'},
]

SUBREDDIT_OPTIONS = [
    {'label': 'r/CryptoCurrency', 'value': 'CryptoCurrency'},
    {'label': 'r/CryptoMarkets', 'value': 'CryptoMarkets'},
    {'label': 'r/coinbase', 'value': 'Coinbase'},
    {'label': 'r/CryptoMoonShots', 'value': 'CryptoMoonShots'},
    {'label': 'r/binance', 'value': 'Binance'}
]

DURATION_OPTIONS = [
    {'label': '3 Days', 'value': '3d'},
    {'label': '7 Days', 'value': '7d'},
    {'label': '30 Days', 'value': '30d'},
    {'label': '60 Days', 'value': '60d'},
]

def time_period(duration):
    end_time = datetime.utcnow()
    if duration == '3d':
        start_time = end_time - timedelta(days=3)
    elif duration == '7d':
        start_time = end_time - timedelta(days=7)
    elif duration == '30d':
        start_time = end_time - timedelta(days=30)
    elif duration == '60d':
        start_time = end_time - timedelta(days=60)
    else:
        raise ValueError("Invalid duration")

    return start_time.timestamp(), end_time.timestamp()

def sentiment_category(sentiment_score):
    if 0 <= sentiment_score <= 20:
        return 'extreme_fear'
    elif 21 <= sentiment_score <= 39:
        return 'fear'
    elif 40 <= sentiment_score <= 59:
        return 'neutral'
    elif 60 <= sentiment_score <= 79:
        return 'greedy'
    else:
        return 'extremely_greedy'
    
    