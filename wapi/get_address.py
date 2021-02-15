import json
from wapi import *
def doge_address():
                 data = json.dumps({'api_key' = "api_key",
                                    'currency' = "DOGE"
                                    'username' = "username"
                                    'action' = 'getnewaddress'
                                    })
                 r = requests.post( wapi_key, data = data)

                 js = json.loads(r.text)
                 return js['address']
def ltc_address():
                data = json.dumps({'api_key' = "api_key",
                                    'currency' = "LTC"
                                    'username' = "username"
                                    'action' = 'getnewaddress'
                                    })
                 r = requests.post( wapi_key, data = data)

                 js = json.loads(r.text)
                 return js['address']
def btc_address():
                data = json.dumps({'api_key' = "api_key",
                                    'currency' = "BTC"
                                    'username' = "username"
                                    'action' = 'getnewaddress'
                                    })
                 r = requests.post( wapi_key, data = data)

                 js = json.loads(r.text)
                 return js['address']
