import csv
import random

drinkercsv = open("drinkers.csv", "r")
dreader = csv.reader(drinkercsv)
beercsv = open("beers.csv", "r")
breader = csv.reader(beercsv)

beers = []

with open('likes.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    for row in breader:
        if row[0] != "name":
            beers.append(row[0])
    for row in dreader:
        if row[0] != "name":
            rdmiter = random.randint(0,4)
            for x in range(0,rdmiter):
                filewriter.writerow([row[0], random.choice(beers)])

drinkercsv.close()
beercsv.close()
        