import csv

file_url = 'files/stock_codes.csv'
with open(file_url, newline='') as f:
    stocks = csv.reader(f, dialect="excel")
    print(type(stocks))
    for stock in stocks:
        print(stock[0])
