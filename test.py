# FILE ONLY FOR PRODUCTION.
# REMOVE THIS FILE BEFORE DEPLOYMENT.

import csv
import pprint # Prettifies json objects

hoursList = []

with open('static/data/hours.csv') as hoursFile:
    next(hoursFile)
    csvReader = csv.reader(hoursFile, delimiter=',')
    for row in csvReader:
        venue = {
            "name": row[0],
            "sunday": row[1],
            "monday": row[2],
            "tuesday": row[3],
            "wednesday": row[4],
            "thursday": row[5],
            "friday": row[6],
            "saturday": row[7]
        }
        hoursList.append(venue)

for venue in hoursList:
    pprint.PrettyPrinter(indent=4).pprint(venue)
