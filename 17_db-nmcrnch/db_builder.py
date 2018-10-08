#JoKaz -- Isaac Jon and Ahnaf Kazi
#SoftDev1 pd6
#K16 -- No Trouble
#2018-10-05

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

open(DB_FILE,'w').close() #Reset DB file

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#Create table for students' grades
command = "" #build SQL stmt, save as string

with open('data/courses.csv', 'r') as file:
    command += "CREATE TABLE grades(code TEXT, mark INTEGER, id INTEGER); "
    reader = csv.DictReader(file)
    for line in reader:
        one = line['code']
        two = line['mark']
        three = line['id']
        command += "INSERT INTO grades "
        command += "VALUES(" + "'" + one + "'" + "," + two + "," + three + "); "

print(command)
c.executescript(command)
#========================================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#Create table for students' grades
command = "" #build SQL stmt, save as string

with open('data/peeps.csv', 'r') as file:
    command += "CREATE TABLE students(name TEXT, age INTEGER, id INTEGER); "
    reader = csv.DictReader(file)
    for line in reader:
        one = line['name']
        two = line['age']
        three = line['id']
        command += "INSERT INTO students "
        command += "VALUES(" + "'" + one + "'" + "," + two + "," + three + "); "

c.executescript(command)

#==========================================================

db.commit() #save changes
db.close()  #close database
