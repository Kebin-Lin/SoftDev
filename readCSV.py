#LinBo - Kevin Lin and Bo Hui Lu
#SoftDev pd6
#K #06: StI/O: Divine your Destiny!
#2018-09-13


import csv

newDict = {}

with open('occupations.csv') as inputFile:
    reader = csv.DictReader(inputFile)

    for row in reader:
         newDict[ row['Job Class'] ] = row['Percentage']


print(newDict)
