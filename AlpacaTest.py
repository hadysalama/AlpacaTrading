import requests
from config import *
import pprint as pp
import time

base_url = "https://paper-api.alpaca.markets"
account_url = "{}/v2/account".format(base_url)
orders_url = "{}/v2/orders".format(base_url)
headers = {
        'APCA-API-KEY-ID': API_KEY_ID,
        'APCA-API-SECRET-KEY': API_SECRET_KEY
    }

#Base Format for a Raw API Request to Alpaca Trading API
r = requests.get(base_url, headers={
    'APCA-API-KEY-ID': API_KEY_ID,
    'APCA-API-SECRET-KEY': API_SECRET_KEY
})

'''
response = r.json()  # Converts JSON Response into a Python Dictionary

print(type(response))  # <class 'dict'> LEGOOOOO

pp.pprint(response)# instead of print(r.content) we neatly print the JSON response
'''

# @return: <class 'dict'>
def get_account():
    r = requests.get(account_url, headers=headers)
    return r.json()


# @return: <class 'dict'>
def get_orders():
    r = requests.get(orders_url, headers=headers)
    return r.json()

# @return: <class 'dict'>
def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(orders_url, json = data, headers=headers)
    return r.json()

print()
#pp.pprint(get_account())

#pp.pprint(create_order('MSFT', 100, 'buy', 'market', 'gtc'))

for i in range(100):
    time.sleep(1)
    create_order('MSFT', 1, 'buy', 'market', 'gtc')

'''
requests.get("https:amazon.com/alexa: Alexa move turn on the lights")

turnonthelight()
'''