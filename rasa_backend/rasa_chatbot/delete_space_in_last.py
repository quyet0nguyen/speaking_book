import csv
import os


locations = []
with open('location_entity/_entity_.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    locations.append([lines[0].rstrip()])

with open("location_entity/_entity_edit.csv", mode ='w') as file: 
   csvwriter = csv.writer(file)
   csvwriter.writerows(locations)