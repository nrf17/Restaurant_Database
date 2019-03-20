import csv
import random

foodfile = open("ddb+_foods.txt", "r")
beerfile = open("ddb+_beer_brands.txt", "r")
manfiles = open("ddb+_manf.txt", "r").read().splitlines()
foodcsv = open("food.csv", "w")
beercsv = open("beers.csv", "w")

with open('items.csv', 'w') as itemcsv:
    itemwriter = csv.writer(itemcsv, delimiter=',')
    foodwriter =  csv.writer(foodcsv, delimiter=',')
    beerwriter =  csv.writer(beercsv, delimiter=',')
    for line in foodfile:
        foodwriter.writerow([(line.strip())])
        itemwriter.writerow([(line.strip())])
    for beerline in beerfile:
        manf = random.choice(manfiles)
        itemwriter.writerow([(beerline.strip())])
        beerwriter.writerow([beerline.strip(), manf.strip()])
    
foodfile.close()
beerfile.close()
foodcsv.close()
beercsv.close()