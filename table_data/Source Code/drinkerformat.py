import csv
import random

namefile = open("formatted_drinker_names.txt", "r")
citystatefile = open("ddb+_city_state.txt").read().splitlines()
addrfile = open("ddb+_ppl_addr.txt", "r")
phonefile = open("formatted_phone_num.txt", "r")

with open('drinkers.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')

    for nameline, phoneline, addrline in zip(namefile, phonefile, addrfile):
        cityline = random.choice(citystatefile)
        cstate = cityline.split(", ")

        filewriter.writerow([nameline.strip(), 
        cstate[0].strip(), cstate[1].strip(), 
        phoneline.strip(), addrline.strip()])

namefile.close()
addrfile.close()
phonefile.close()

        