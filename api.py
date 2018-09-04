#Q.1-Use the "https://api.forismatic.com/api/1.0/" api to get random quotes using the correct endpoints.

import requests
data=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
print(data.status_code)
import json
a=data.json()
print(type(a))
print(a["quoteText"])
