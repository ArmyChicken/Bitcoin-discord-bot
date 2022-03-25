from requests import Request, Session
import json

def getbitcoin():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = {
     'slug' : 'bitcoin',
    }

    headers =  {
     'Accepts' : 'aplication/json',
     'X-CMC_PRO_API_KEY': 'd8a7e9cc-e4d7-4c9e-906f-96ee0c7aa7be'
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    return(f"BTC={round(json.loads(response.text)['data']['1']['quote']['USD']['price'],2)}$")