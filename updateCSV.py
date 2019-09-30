import csv

running = True

while(running):
    venue = input("Venue: ")
    sunday = input("Sunday: ")
    monday = input("Monday: ")
    tuesday = input("Tuesday: ")
    wednesday = input("Wednesday: ")
    thursday = input("Thursday: ")
    friday = input("Friday: ")
    saturday = input("Saturday: ")

    with open('static/data/hours.csv', mode='a') as hoursCSV:
        hoursWriter = csv.writer(hoursCSV, delimiter=',',
                                 quotechar='"', quoting=csv.QUOTE_MINIMAL)
        hoursWriter.writerow([venue, sunday, monday, tuesday,
                              wednesday, thursday, friday, saturday])
    if input("Keep going? Y/N: ") == "N":
        running = False
