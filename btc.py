from requests import Request, Session
import json

def getbitcoin():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = {
     'slug' : 'bitcoin',
    }

    headers =  {
     'Accepts' : 'aplication/json',
     'X-CMC_PRO_API_KEY': 'your api key'
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    return(f"BTC={round(json.loads(response.text)['data']['1']['quote']['USD']['price'],2)}$")
