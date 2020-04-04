## Web scraper to pull stock data from Google and store and compare prices
from selenium import webdriver
## Have to import your own list of stocks to watch
## Stocks should come as a dictionary with the format (key : pair) -> ('stock' : target_price)
from stocks_to_watch import stocks
import time

## Create empty dictionary to store scraped values
todays_stocks = {}
saved_stocks = []

class StockScraper():
    """Create all methods to scrape stock info, compare values for current values and print to a text
    file to save each run's results."""

    def __init__(self, stocks):
        self.browser = webdriver.Chrome()
        self.stocks = stocks
        stock_names = stocks.keys()
        self.stock_names = stock_names

    def gather_stock_info(self):
        """Scrape the stock prices off of Google."""
        self.browser.get("https://www.google.com/search?q=alphabet+stock&oq=al&aqs=chrome.1.69i57j69i59j35i39j0j69i60l4.2188j1j7&sourceid=chrome&ie=UTF-8")
        for stock in self.stocks:
            search_bar = self.browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input')
            search_button = self.browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/button')
            search_bar.clear()
            search_bar.send_keys(f"{stock} stock")
            search_button.click()
            stock_price = self.browser.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section[1]/div/g-card-section/span[1]/span/span[1]')
            todays_stocks[stock] = stock_price.text.replace(',','')
        print(todays_stocks)

    def compare_price(self):
        """Compare target prices to current prices for scraped stocks."""
        for name in self.stock_names:
           if float(todays_stocks[name]) < float(stocks[name]):
               print(f"{name} is below your target price. Buy now!")
           else:
               pass
               #print(f"Do not buy {name}.")

## Create a method that writes (appends) this list to a file with the todays_stocks
    def record_prices(self):
        with open('stocks_tracker.txt', 'a') as f:
            current_time = time.ctime(time.time())
            f.write(f"\n\n{current_time}\n")
            copy_of_stocks = []
            for stock_name, value in todays_stocks.items():
                messages = f"\n{stock_name} : {value}"
                saved_stocks.append(messages)
            f.writelines(saved_stocks)

stocks_to_watch = StockScraper(stocks)
stocks_to_watch.gather_stock_info()
stocks_to_watch.compare_price()
stocks_to_watch.record_prices()
