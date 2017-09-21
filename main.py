import requests
import time
url = 'https://api.coinbase.com/v2/prices/USD/spot?'
req = requests.get(url)
data = req.json()
bb = (data['data'][0]['amount'])
while True:
    print "1 BTC = %s USD" % bb
    time.sleep(2)