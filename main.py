#!/usr/bin/env python3
# imports
import requests
import time
from tkinter import *
import random

# variables
test = 'https://api.nicehash.com/api?method=stats.provider.ex&addr=37sCnRwMW7w8V7Y4zyVZD5uCmc9N1kZ2Q8&callback=jQuery111304118770088094035_1506738346881&_=1506738346882'
url = 'https://api.coinbase.com/v2/prices/USD/spot?'



# def function to update
def update_bitcoin_ui():

    # update the data sourced form the website
    req = requests.get(url)
    data = req.json()
    bit = (data['data'][0]['amount'])

    # update the gui to reflect new value
    thelabel.config(text = "1 BTC = %s USD" % bit)

    # verify the Ui is updating
    #thelabel.config(text=str(random.random()))
    root.after(1000, update_bitcoin_ui)

# gui workspace
root = Tk()
thelabel = Label(root, text = "")

# set more of the gui and launch the ui
thelabel.pack()
root.after(1000, update_bitcoin_ui)
root.mainloop()



# loop for printing price
"""
while True:

    bit_string_var.set("1 BTC = %s USD" % bit)
    print("1 BTC = %s USD" % bit)
    time.sleep(5)
"""