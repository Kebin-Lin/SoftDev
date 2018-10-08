#Waffle -- Kevin Lin and Ahnaf Kazi
#SoftDev1 pd6
#K17 -- Average
#2018-10-06

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
students = {} #Dictionary to hold students

for row in c.execute("SELECT * FROM students"): #Goes through all rows in table "students"
    studict = {} #Create a dictionary to hold all information for this particular student
    studict['name'] = row[0]
    studict['grades'] = [] #Create empty list to hold grades for later
    students[row[2]] = studict #It's a dictionary, inside a dictionary!! Key for the big dictionary is the student id

c.execute("CREATE TABLE peeps_avg(id INTEGER, avg REAL)") #Create new table for averages

for studentid in students.keys(): #Goes through all student ids
    for row in c.execute("SELECT mark FROM grades WHERE grades.id = {0}".format(studentid)):
        students[studentid]['grades'].append(row[0]) #Adds each mark for each id to a list for the student

    lst = students[studentid]['grades']
    avg = sum(lst)/len(lst) #Changes the list to an average
    students[studentid]['grades'] = str(avg) #Stores avg as a string in the dictionary
    print(students[studentid]['name'] + ' ' + students[studentid]['grades']) #Print sudent name and average

    c.execute("INSERT INTO peeps_avg VALUES({0}, {1})".format(studentid, avg)) #Inserts values into peeps_avg

db.commit()
db.close()
