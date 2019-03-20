import csv
import random

billcsv = open("bills.csv", "r")
breader = csv.reader(billcsv)
sellcsv = open("sells.csv", "r")
sreader = csv.reader(sellcsv)

bills = []
sells = {}

with open('transactions.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    for row in breader:
        bills.append(row)
    for row in sreader:
        bar = row[1]
        if bar in sells:
            curritems = sells[bar]
            curritems.append(row[2])
            sells[bar] = curritems
        else:
            sells[bar] = [row[2]]
    for bill in bills:
        bar = bill[4]
        items = sells[bar]
        for x in range(0, random.randint(4,11)):
            item = random.choice(items)
            filewriter.writerow([bill[0], item, random.randint(1,7)])

billcsv.close()
sellcsv.close()