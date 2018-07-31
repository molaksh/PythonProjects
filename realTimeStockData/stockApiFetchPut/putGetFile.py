import json
import urllib2 
import pymongo
from pymongo import MongoClient

#username and password needed
client = MongoClient("mongodb://<username>:<password>@cluster0-shard-00-00-phpjx.mongodb.net:27017,cluster0-shard-00-01-phpjx.mongodb.net:27017,cluster0-shard-00-02-phpjx.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

db = client.myDB
db.quote.drop()
db.crypto.drop()

#generate Quote URL
def generateQuoteURL(mystring):
    baseURL = 'https://api.iextrading.com/1.0/stock/'
    quote = '/quote'
    quoteURL = baseURL + mystring + quote
    return quoteURL

#generate Crypto URL
def generateCryptoURL(mystring):
    baseURL = 'https://www.alphavantage.co/query?'
    function = 'function=DIGITAL_CURRENCY_INTRADAY&symbol='
    symbol = mystring
    market = '&market=USD&apikey='
    
    #add valid api key
    apiKey = 'APIKEYNEEDED!'
    
    cryptoURL = baseURL + function + symbol + market + apiKey
    return cryptoURL

#getting data from webApi
def webApiCall(url):
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    return data

#remove '.' in key value of json -> not used 
def remove_dot_key(cdata): 
    for key in cdata.keys(): 
        new_key = key.replace(".","")
        if new_key != key:
            cdata[new_key] = cdata[key]
            del cdata[key]
    return cdata

#get price value from crypto data of alpha vantage
def getPrice(temp):
    for item in temp:
        price = temp[item]['1b. price (USD)']
        break
    return price

#process large data from alpha vantage to required data
def processData(tempData):
    try:
        crypto_price = getPrice(tempData['Time Series (Digital Currency Intraday)'])
        crypto_name = tempData['Meta Data']['3. Digital Currency Name']
        crypto_code = tempData['Meta Data']['2. Digital Currency Code']
        
        json_data = {"cryptoName" : crypto_name, "cryptoCurrencyCode" : crypto_code, "cryptoPrice" : crypto_price}
        
        print (json_data)
        return json_data
    except:
        print("Error in web Api Json Output")
        print(tempData)
        return tempData

#push Quote data into DB
def putQuoteDataToDb(dataToPut):
    db.quote.insert(dataToPut)

#push Crypto data into DB
def putCryptoDataToDb(dataToPut):
    db.crypto.insert(dataToPut)


#get from DB -> not used right now
def getFromDb(getQuery):
    db.testcollection.find(getQuery)

#get stock info and put to DB
class updateDatabase:
    def updateStockQuote(self, stock_list):
        print("\nUpdating Stock quotes")
        for stock in stock_list:
            print(stock)
            qurl = generateQuoteURL(stock)
            qData = webApiCall(qurl)
            putQuoteDataToDb(qData)  
        return  

    def updateCryptoQuote(self, crypto_currency_list):
        print("\nUpdating Crypto Currencies")
        for each in crypto_currency_list:
            print(each)
            crurl = generateCryptoURL(each)
            cData = webApiCall(crurl)
            cReqData = processData(cData)
            putCryptoDataToDb(cReqData)            
        return
    
