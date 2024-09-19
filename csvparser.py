
#This is a sample code for parsers such as csv, JSON
import csv
with open('samplecsv.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], row['City'], row['Country'])

