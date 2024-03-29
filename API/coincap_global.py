import json
import requests
from datetime import datetime

currency = 'JPY'
global_url = "https://api.coinmarketcap.com/v2/global/?convert=" + currency

requests = requests.get(global_url)
results = requests.json()

active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = results['data']['quotes'][currency]['total_market_cap']
global_volume = results['data']['quotes'][currency]['total_volume_24h']

active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
active_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)
bitcoin_percentage_string = '{:,}'.format(bitcoin_percentage)
last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')

print("There are currenctly " + active_currencies_string + ' active cryptocurrencies and ' + active_markets_string +' active markets.')
print("the global cap of all cryptos is" + active_cap_string +' and the 24h global volume is'+ global_volume_string +'!!')
print("Bitcoin\s total percentage of the global cap is "+ bitcoin_percentage_string +'.')
print()
print("this information was last updates on " + last_updated_string + '!!')
