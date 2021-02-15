import json
from wapi import "

data = json.dumps({'api_key' = "api_key",
                   'currency' = "currency",
                   'username' = "username"
                   'action' = 'getnewaddress'
                   })
r = requests.post( wapi_key, data = data)

js = json.loads(r.text)
return js['address']
