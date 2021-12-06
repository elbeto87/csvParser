import csv

with open('csv-demo') as csvFile:
    csvFile = dict(csv.reader(csvFile))

for alumnos in csvFile:
    print(alumnos, csvFile[alumnos])


