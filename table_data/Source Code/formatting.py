import csv
import random

namefile = open("ddb+_bars.txt", "r")
citystatefile = open("ddb+_city_state.txt").read().splitlines()
addrfile = open("formatted_address.txt", "r")
hoursfile = open("formatted_times.txt", "r")
phonefile = open("formatted_phone_num.txt", "r")

with open('bars.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    name = []
    opening = []
    closing = []
    license_id = []
    phone_num = []
    street = []
    city = []
    state = []

    for nameline, hoursline, phoneline, addrline in zip(namefile, hoursfile, phonefile, addrfile):
        name.append(nameline)

        hours = hoursline.split(',')
        opening.append(hours[0])
        closing.append(hours[1])

        phone_num.append(phoneline)

        street.append(addrline)

        cityline = random.choice(citystatefile)
        cstate = cityline.split(", ")
        city.append(cstate[0])
        state.append(cstate[1])
        lid = cstate[1] + str(random.randint(10000, 99999))
        license_id.append(lid)

    for x in range(0,len(name)):
        filewriter.writerow([name[x].strip(), opening[x].strip(), 
        closing[x].strip(), license_id[x].strip(), 
        phone_num[x].strip(), street[x].strip(), city[x].strip(), 
        state[x].strip()])

namefile.close()
addrfile.close()
hoursfile.close()
phonefile.close()