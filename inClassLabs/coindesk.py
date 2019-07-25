import requests
import time
import dns
from pymongo import MongoClient

client = MongoClient('mongodb+srv://dbuser:M4ng0357!@cluster0-ubk6k.azure.mongodb.net/test?retryWrites=true&w=majority')
db = client.test

while True:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if r.status_code == 200:
        data = r.json()
        print(data)
        time.sleep(60)
    else:
        exit()