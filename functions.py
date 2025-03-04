from pyfiglet import Figlet
import json
import httpx

def send_discord_alert(message: str):
    DISCORD_WEBHOOK_URL = get_config_data()['DISCORD_WEBHOOK']
    try:
        httpx.post(DISCORD_WEBHOOK_URL, json={'content': f'{message}'})
    except:
        pass

def send_telegram_alert(message: str):
    TELEGRAM_API_INFO = get_config_data()
    TELEGRAM_BOT_TOKEN = TELEGRAM_API_INFO['TELEGRAM_BOT_TOKEN']
    TELEGRAM_CHAT_ID = TELEGRAM_API_INFO['TELEGRAM_CHAT_ID']
    TELEGRAM_URL = "https://api.telegram.org/bot" + TELEGRAM_BOT_TOKEN + "/sendMessage"
    PAYLOAD = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    try:
        httpx.post(url=TELEGRAM_URL, data=PAYLOAD)
    except:
        pass
    
def display_logo() -> None:
    """Display Sol logo."""
    print("\033c\n", end="")
    print("-" * 51, "\n" + Figlet(font='small').renderText('Sol Sniper\n') + "-" * 51 + "\n")

def get_config_data() -> dict:
    """Fetch config file data.
    Returns: dict"""
    with open('config.json', 'r') as config_file:
            return json.load(config_file)
        
def load_wallets() -> dict:
    """Returns all wallets stored in wallets.json."""
    with open('wallets.json', 'r') as wallets_file:
        return json.load(wallets_file)
    
def get_crypto_price(crypto: str) -> float:
    """Returns crypto price."""
    API_BINANCE = f"https://www.binance.com/api/v3/ticker/price?symbol={crypto}USDT"
    crypto_price =float(httpx.get(API_BINANCE).json()['price'])
    return crypto_price

def get_timestamp_formatted(unix_timestamp: int) -> str:
    """Returns timestamp formatted based on a unix timestamp."""
    if unix_timestamp < 60:
        return f"{unix_timestamp} seconds"
    elif unix_timestamp < 3600:
        minutes = unix_timestamp // 60
        seconds = unix_timestamp % 60
        return f"{minutes} minute{'s' if minutes > 1 else ''} and {seconds} second{'s' if seconds > 1 else ''}"
    elif unix_timestamp < 86400:
        hours = unix_timestamp // 3600
        minutes = (unix_timestamp % 3600) // 60
        return f"{hours} hour{'s' if hours > 1 else ''}, {minutes} minute{'s' if minutes > 1 else ''}"
    elif unix_timestamp < 604800:
        days = unix_timestamp // 86400
        hours = (unix_timestamp % 86400) // 3600
        return f"{days} day{'s' if days > 1 else ''}, {hours} hour{'s' if hours > 1 else ''}"
    elif unix_timestamp < 2629746:  # Approximately a month
        weeks = unix_timestamp // 604800
        days = (unix_timestamp % 604800) // 86400
        return f"{weeks} week{'s' if weeks > 1 else ''}, {days} day{'s' if days > 1 else ''}"
    else:
        months = unix_timestamp // 2629746  # Approximately a month
        days = (unix_timestamp % 2629746) // 86400
        return f"{months} month{'s' if months > 1 else ''}, {days} day{'s' if days > 1 else ''}" 