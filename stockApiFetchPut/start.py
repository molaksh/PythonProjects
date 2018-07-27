import time
from putGetFile import updateDatabase

stock_list = ["aapl","twtr","tsla","fb","msft","dis","gpro",
                "sbux","f","baba","fit","aaba","ge","bac","jcp"
                ,"nflx","vlo","feye","nvda","amzn","crm","goog"]

crypto_currency_list1 = ["BTC","ETH","BCH","LTC"]
crypto_currency_list2 = ["DOGE","XRP","QTUM","ETC"]
crypto_currency_list3 = ["XLM","NEO","ZEC","XMR"]
crypto_currency_list4 = ["DASH","BTG","LSK","OMG"]

crypto_currency_list = [crypto_currency_list1,crypto_currency_list2,crypto_currency_list3,crypto_currency_list4]

def main():
    ud = updateDatabase()
    ud.updateStockQuote(stock_list)
    for crypto in crypto_currency_list:
        time.sleep(60)
        ud.updateCryptoQuote(crypto)
        
if __name__ == '__main__':
    main() 