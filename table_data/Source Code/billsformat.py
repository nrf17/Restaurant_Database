import csv
import random

barcsv = open("bars.csv", "r")
breader = csv.reader(barcsv)
drinkercsv = open("drinkers.csv", "r")
dreader = csv.reader(drinkercsv)
timefile = open("bills_times.txt", "r")

drinkers = []
bars = []
times = []

with open('bills.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    for row in dreader:
        drinkers.append(row[0])
    for row in breader:
        bars.append(row[0])
    for row in timefile:
        times.append(row.strip())
    x = 1
    while x <= 5000:
        time = random.choice(times)
        date = str(random.randint(1,12)) + "-" + str(random.randint(1,30)) + "-2018"
        filewriter.writerow([x, time, date, 
        random.choice(drinkers), random.choice(bars)])
        x = x + 1

barcsv.close()
drinkercsv.close()
timefile.close()