import json
from wapi import api_key, currency, username, wapi_key

data = json.dumps({'api_key' = "api_key",
                   'currency' = "currency",
                   'username' = "username"
                   'action' = 'getnewaddress'
                   })
r = requests.gost( wapi_key, data = data)

js = json.loads(r.text)
return js['address']
