#Team Penguins -- Kevin Lin, Angela Tom
#SoftDev Pd6
#K10 -- Jinja Tuning
#2018-09-24

import csv,random
from flask import Flask, render_template
import util.occupation as occupation
app = Flask(__name__) #Create instance of class Flask

@app.route("/") #Assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__) #Where will this go?
    return "No hablo queso!"


@app.route('/occupations')
def occupations():
    lst = occupation.createTable()
    ans = occupation.selectRandOccupation() # variable ans is a random occupation
    return render_template('occupations.html', input = lst,r = ans) # render template


if __name__ == "__main__":
    app.debug = True
    app.run()
