import csv
import random

namefile = open("ddb+_bartenders.txt", "r")
citystatefile = open("ddb+_city_state.txt").read().splitlines()

with open('bartenders.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')

    for nameline in namefile:
        cityline = random.choice(citystatefile)
        cstate = cityline.split(", ")

        filewriter.writerow([nameline.strip(), cstate[1].strip()])

namefile.close()