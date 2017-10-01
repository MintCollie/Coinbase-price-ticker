#!/usr/bin/env python3
import requests
import time
test = 'https://api.nicehash.com/api?method=stats.provider.ex&addr=37sCnRwMW7w8V7Y4zyVZD5uCmc9N1kZ2Q8&callback=jQuery111304118770088094035_1506738346881&_=1506738346882'
url = 'https://api.coinbase.com/v2/prices/USD/spot?'
req = requests.get(url)
data = req.json()
bit = (data['data'][0]['amount'])
while True:
    print("1 BTC = %s USD" % bit)
    time.sleep(60)
