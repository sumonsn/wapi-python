import requests
import json
from __init__ import *
from config import *


def get_address(currency):
                 data = json.dumps({'apikey':api_key,
                                    'currency':currency,
                                    'username':str(username),
                                    'action':'getnewaddress'
                                    })

                 r = requests.post(str(wapi_url), data = data)

                 js = json.loads(r.text)
                 return js['address']


btc = get_address("btc")
doge = get_address("doge")
ltc = get_address("ltc")
a = "Your doge address is :\n"
b = "Your ltc address is :\n"
c = "Your btc address is :\n"

def addresses():
             addresses = print(str(a), doge +"\n"+ str(b), ltc + "\n" + str(c),btc )
             return addresses
