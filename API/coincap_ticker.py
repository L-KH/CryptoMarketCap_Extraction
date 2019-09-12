import json
import requests

while true:

    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array'

    limit = 100
    start = 1
    sort = 'rank'
    convert = 'USD'



    choice = input("Do you want to enter any custom parametres? (y/N)")
    if choice == 'y':
        limit = input("what is the custom limit?")
        start = input("what is the custom start numbers?")
        sort = input("what do you want to sort by? :(example: id, rank)")
        convert = input("what is your local currency? :(example: USD, JPY)")

    ticker_url += '&limit=' + str(limit) + '&sort=' + sort + '&start=' + str(start) + '&convert=' + convert
    request = requests.get(ticker_url)
    results = request.json()
    print(json.dumps(results, sort_keys = True, indent=4))
    data = results['data']
    print()
    for currency in data:
        rank = currency['rank']
        name = currency['name']
        symbol = currency['symbol']

        circulating_supply = int(currency['circulating_supply'])
        total_supply = int(currency['total_supply'])

        quotes = currency['quotes'][convert]
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        volume_string = '{:,}'.format(volume)
        market_cap_string = '{:,}'.format(market_cap)
        circulating_supply_string = '{:,}'.format(circulating_supply)
        total_supply_string = '{:,}'.format(total_supply)

        print(str(rank)+ ' : '+ name + '(' + symbol + ')')
        print('Market cap: \t\t$ ' + market_cap_string)
        print('Price: \t\t\t$' + str(price))
        print('24h volume: \t\t$' + volume_string)
        print('Hour change:\t\t' + str(hour_change) + '%')
        print('Day change:\t\t' + str(day_change) + '%')
        print('week change:\t\t' + str(week_change) + '%')
        print('total supply:\t\t' + total_supply_string)
        print('Circulating supply:\t' + circulating_supply_string)
        print('percentage of coins in circulating:' + str(int(circulating_supply/ total_supply)))
        print()

    choice = input('Again ? (y/n):')
    if choice == 'n':
        break
