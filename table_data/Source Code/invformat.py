import csv
import random

barcsv = open("bars.csv", "r")
breader = csv.reader(barcsv)
itemcsv = open("items.csv", "r")
ireader = csv.reader(itemcsv)

items = []

with open('inventory.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    for row in ireader:
        items.append(row[0])
    for row in breader:
        for x in range(15,55):
            count = str(random.randint(200, 500))
            filewriter.writerow([count,row[0], 
            items[x]])

barcsv.close()
itemcsv.close()