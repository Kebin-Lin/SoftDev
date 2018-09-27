from flask import Flask, render_template, request
app = Flask(__name__) #Create instance of class Flask

@app.route("/") #Assign fxn to route
def hello_world():
    print(app)
    return render_template("input.html")

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return render_template("auth.html",username = request.args["username"],
                               reqMethod = request.args["sub1"])

if __name__ == "__main__":
    app.debug = True
    app.run()
