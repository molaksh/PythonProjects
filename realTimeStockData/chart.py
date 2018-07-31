import json
import urllib2 
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://<username>:<password>@cluster0-shard-00-00-phpjx.mongodb.net:27017,cluster0-shard-00-01-phpjx.mongodb.net:27017,cluster0-shard-00-02-phpjx.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = client.tempDB
db.temp.drop()


#generate Crypto URL
def generateCryptoURL(mystring):
    baseURL = 'https://www.alphavantage.co/query?'
    function = 'function=DIGITAL_CURRENCY_INTRADAY&symbol='
    symbol = mystring
    market = '&market=USD&apikey='
    apiKey = 'APIKEYNEEDED!'
    cryptoURL = baseURL + function + symbol + market + apiKey
    return cryptoURL


#getting data from webApi
def webApiCall(url):
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    return data


string1 = "BTC"
cryURL = generateCryptoURL(string1)
print(cryURL)
data1 = webApiCall(cryURL)



for item in data1['Time Series (Digital Currency Intraday)']:
    price = data1['Time Series (Digital Currency Intraday)'][item]['1a. price (USD)']
    temp =  { '_id' : item , 'price' : price }
    db.temp.insert(temp)

dbOut = db.temp.find()

df = pd.DataFrame(list(dbOut))

df = df.sort_values(by=['_id'])
df['_id'] = df['_id'].astype('datetime64[ns]')
df['price'] = df['price'].astype('float64')
df.plot(x='_id', y='price')
plt.show()
