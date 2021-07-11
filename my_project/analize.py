import csv

file_url = 'strages_data/002900_signal.csv'

with open(file_url, encoding="utf-16") as f:
    datas = csv.reader(f, dialect="excel")
    for data in datas:
        print(data)
