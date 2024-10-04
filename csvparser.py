
#This is a sample code for parsers such as csv, JSON
import csv
import pandas
try:
    with open('samplecsv.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Name'], row['City'], row['Country'])
except Exception as e:
    print(e)

#Sample using pandas
print("\n ********************* Sample using Pandas library *****************")
panda_test = pandas.read_csv("samplecsv.csv")
print(panda_test.to_string())