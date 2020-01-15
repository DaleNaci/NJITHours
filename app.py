import csv
import os

from flask import Flask, render_template, url_for, request


app = Flask(__name__)

hoursList = [] # Might rename variable

currentFolder = os.path.dirname(os.path.abspath(__file__))
csvFile = os.path.join(currentFolder, "static/data/hours.csv")

with open(csvFile) as hoursCSV:
    next(hoursCSV)
    csvReader = csv.reader(hoursCSV, delimiter=',')
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


@app.route('/')
def index():
    return render_template('index.html', venues=hoursList)

if __name__ == "__main__":
    app.run(debug=True)
