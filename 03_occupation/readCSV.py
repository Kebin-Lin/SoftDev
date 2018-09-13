#LinBo - Kevin Lin and Bo Hui Lu
#SoftDev pd6
#K #06: StI/O: Divine your Destiny!
#2018-09-13


import csv,random

occDict = {}

with open('occupations.csv') as infile:
    reader = csv.DictReader(infile)

    for row in reader:
         occDict[ row['Job Class'] ] = row['Percentage']

occDict.pop('Total')

for i in occDict.keys():
     occDict[i] = eval(occDict[i]) #Changes strings into numbers

print occDict

def randomOcc():
     randNum = random.random() * 100
     currNum = 0

     for i in occDict.keys():
          currNum += occDict[i]
          if randNum <= currNum:
               return i
     return randomOcc() #If the number generated is greater than the total prb, retry
