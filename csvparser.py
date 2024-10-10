
#This is a sample code for parsers such as csv, JSON
import csv
import pandas
try:
    with open('samplecsv.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not row['Name']:
                print("Name is missing")
            elif not row['Email']:
                print("Email is missing")
            elif not row['DOB']:
                print("DOB is missing")
            else:
                print(row['Name'], row['Email'], row['DOB'])
except Exception as e:
    print(e)

#Sample using pandas
print("\n ********************* Sample using Pandas library *****************")
panda_test = pandas.read_csv("samplecsv.csv")
print(panda_test.to_string())