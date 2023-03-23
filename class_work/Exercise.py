import csv 

with open("voucher.csv", 'r') as data:
    for file in csv.DictReader(data):
        print(file)