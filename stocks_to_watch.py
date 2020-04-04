## Script to store the stocks you want to watch and the prices you'd buy them at
## Enter in the dictionary the "name" : "stock symbol" pair for each company you want to watch
stock_names = {"Apple" : "AAPL","Facebook" : "FB", "Microsoft" : "MSFT", "Amazon" : "AMZN", "Tesla" : "TSLA"}

## Enter the target prices that you would buy at
prices = [225, 145, 145, 1750, 375]

stocks = {}
count = 0

for stock in stock_names:
    stocks[stock] = prices[count]
    count += 1

print(stocks)