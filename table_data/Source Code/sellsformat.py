import csv
import random

barcsv = open("bars.csv", "r")
breader = csv.reader(barcsv)
itemcsv = open("items.csv", "r")
ireader = csv.reader(itemcsv)
beercsv = open("beers.csv", "r")
beerreader = csv.reader(beercsv)

items = []
beer = {}

x = 4.0
for row in beerreader:
    beer[row[0]] = [x, x+.25]
    x = x+0.25

with open('sells.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    for row in ireader:
        items.append(row[0])
    for row in breader:
        for x in range(0,25):
            itemind = random.randint(0,54)
            item = items[itemind]
            price = ""
            if(itemind >= 15):
                pricerange = beer[item]
                price = str(random.uniform(pricerange[0], pricerange[1]))
            else:
                price = str(random.uniform(2, 12))
            ind = price.find('.')
            price = price[:ind+3]
            filewriter.writerow([price,row[0], 
            item])

barcsv.close()
itemcsv.close()