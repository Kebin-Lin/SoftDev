#Kevin Lin
#SoftDev Pd6
#K08 -- Fill Yer Flask
#2018-09-20

from flask import Flask
app = Flask(__name__) #Create instance of class Flask

@app.route("/") #Assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__) #Where will this go?
    return "No hablo queso!"

@app.route("/info")
def info():
    return("This website was created for Software Development")

@app.route("/greetings")
def greetings():
    return("Hello, fellow human being. How are you doing today?")

if __name__ == "__main__":
    app.debug = True
    app.run()
