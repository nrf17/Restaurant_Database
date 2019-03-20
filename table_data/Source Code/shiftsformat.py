import csv
import random

bartendercsv = open("bartenders.csv", "r")
btreader = csv.reader(bartendercsv)
datecsv = open("billsdate.csv", "r")
dreader = csv.reader(datecsv)

bartenders = []

with open('shifts.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    x = 0
    for row in btreader:
        bartenders.append(row)
    for row in dreader:
        opening = row[2]
        closing = row[3]
        opener = bartenders[x]
        x = x+1
        if x == len(bartenders):
            x=0
        filewriter.writerow([row[1], opener[0], 
        opening, closing, row[0]])


bartendercsv.close()
datecsv.close()