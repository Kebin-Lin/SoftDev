from flask import Flask
app = Flask(__name__) #Create instance of class Flask

@app.route("/") #Assign fxn to route
def hello_world():
    return "No hablo queso!"


if __name__ == "__main__":
    app.debug = True
    app.run()
