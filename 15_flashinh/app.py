#Team KateLin
#Kaitlin Wan + Kevin Lin
#SoftDev1 pd6
#K 14: Oh yes, perhaps I do…
#2018-10-03

from flask import Flask,request,render_template,session,url_for,redirect,flash
from util import auth
import os

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = open("secret.txt","r").read()


@app.route('/')
def hello(badWaters = "False"):

    if 'user' in session: #Redirect to logged in page if logged in
        return redirect('/loggedin')

    if "badWaters" in request.args: #Displayed when trying to go to /loggedin without being logged in
        login = "You are treading in BAD waters!!"
        flash(login)
        return render_template("template.html")

    if not("user" in request.args): #Default page
        return render_template("template.html")

    login = auth.checkInfo(request.args["user"],request.args["pass"])
    if login != "Login Successful": #Page with error msg
        flash(login)
        return render_template("template.html")

    else:
        session['user'] = request.args["user"]

        return redirect('/loggedin')

    #Simple HomePage!

@app.route('/loggedin')
def login():
    if 'user' in session:
        dict = request.form
        return render_template('welcome.html', name = session['user'])
    else:
        return redirect(url_for("hello", badWaters = "True"))

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for("hello"))

if __name__ == '__main__':
    app.debug = True
    app.run()
